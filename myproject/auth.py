from passlib.context import CryptContext
import crud
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")


def get_hero_secret_hash(hero_secret):
    return pwd_context.hash(hero_secret)


def verify_secret(plain_secret, hashed_secret):
    return pwd_context.verify(plain_secret, hashed_secret)


def authenticate_hero(db: Session, hero_name: str, hero_secret: str):
    hero = crud.get_hero_by_name(db, hero_name)
    if not hero:
        return False
    if not verify_secret(hero_secret, hero.hero_secret):
        return False
    return hero


def create_access_token(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # Default to 15 minutes of expiration time if ACCESS_TOKEN_EXPIRE_MINUTES variable is empty
        expire = datetime.utcnow() + timedelta(minutes=15)
    # Adding the JWT expiration time case
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


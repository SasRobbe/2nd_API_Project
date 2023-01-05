from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

# For auth, use a hero and their secret
# Atm, the only endpoint that needs auth is get /lootboxes
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import auth
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# make a new lootbox (must be a unique name)
@app.post("/lootboxes/", response_model=schemas.Lootbox)
def create_lootbox(lootbox: schemas.LootboxCreate, db: Session = Depends(get_db)):
    db_lootbox = crud.get_lootbox_by_name(db, lootbox_name=lootbox.lootbox_name)
    if db_lootbox:
        raise HTTPException(status_code=400, detail="There's already a lootbox with this name, be more creative")
    return crud.create_lootbox(db=db, lootbox=lootbox)


# get all lootboxes and there items
@app.get("/lootboxes/", response_model=list[schemas.Lootbox])
def read_lootboxes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    lootboxes = crud.get_lootboxes(db, skip=skip, limit=limit)
    return lootboxes


# get a specific lootbox
@app.get("/lootboxes/{lootbox_id}", response_model=schemas.Lootbox)
def read_lootbox(lootbox_id: int, db: Session = Depends(get_db)):
    db_lootbox = crud.get_lootbox(db, lootbox_id=lootbox_id)
    if db_lootbox is None:
        raise HTTPException(status_code=404, detail="Too creative, no one has thought of this lootbox name before.")
    return db_lootbox


# make items for a lootbox
@app.post("/lootboxes/{lootbox_id}/items/", response_model=schemas.Item)
def create_item_for_lootbox(
    lootbox_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_lootbox_item(db=db, item=item, lootbox_id=lootbox_id)


# get all items
@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


# make a new hero
@app.post("/heroes/")
def create_hero(hero: schemas.HeroCreate, db: Session = Depends(get_db)):
    db_hero = crud.get_hero_by_name(db, hero_name=hero.hero_name)
    if db_hero:
        raise HTTPException(status_code=400, detail="There's already a hero with this name, be more creative")
    return crud.create_hero(db=db, hero=hero)


# get all heroes
@app.get("/heroes/", response_model=list[schemas.Hero])
def read_heroes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    heroes = crud.get_heroes(db, skip=skip, limit=limit)
    return heroes


# delete a hero by name
@app.delete("/heroes/{id}")
def delete_hero(id: int, db: Session = Depends(get_db)):
    db_hero = crud.get_hero_by_id(db, id=id)
    if db_hero is None:
        raise HTTPException(status_code=404, detail="Too creative, no one has thought of this hero name before.")
    crud.delete_hero(db=db, id=id)
    return {"delete request": "success"}


# update a hero
@app.put("/heroes/{id}")
def update_hero(id: int, update: schemas.HeroUpdate, db: Session = Depends(get_db)):
    db_hero = crud.get_hero_by_id(db=db, id=id)
    if db_hero is None:
        raise HTTPException(status_code=404, detail="Too creative, no one has thought of this hero name before.")
    return crud.update_hero(db=db, id=id, update=update)


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #Try to authenticate the user
    hero = auth.authenticate_hero(db, form_data.username, form_data.password)
    if not hero:
        raise HTTPException(
            status_code=401,
            detail="Incorrect login credits",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": hero.hero_name}
    )
    #Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}
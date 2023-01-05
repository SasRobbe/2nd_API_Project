from sqlalchemy.orm import Session

import models
import schemas
import auth


def get_lootbox(db: Session, lootbox_id: int):
    return db.query(models.Lootbox).filter(models.Lootbox.id == lootbox_id).first()


def get_lootbox_by_name(db: Session, lootbox_name: str):
    return db.query(models.Lootbox).filter(models.Lootbox.lootbox_name == lootbox_name).first()


def get_lootboxes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lootbox).offset(skip).limit(limit).all()


def create_lootbox(db: Session, lootbox: schemas.LootboxCreate):
    db_lootbox = models.Lootbox(lootbox_name=lootbox.lootbox_name)
    db.add(db_lootbox)
    db.commit()
    db.refresh(db_lootbox)
    return db_lootbox


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_lootbox_item(db: Session, item: schemas.ItemCreate, lootbox_id: int):
    db_item = models.Item(**item.dict(), owner_id=lootbox_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_hero(db: Session, hero_id: int):
    return db.query(models.Hero).filter(models.Hero.id == hero_id).first()


def get_hero_by_name(db: Session, hero_name: str):
    return db.query(models.Hero).filter(models.Hero.hero_name == hero_name).first()


def get_hero_by_id(db: Session, id: int):
    return db.query(models.Hero).filter(models.Hero.id == id).first()


def get_heroes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hero).offset(skip).limit(limit).all()


def create_hero(db: Session, hero: schemas.HeroCreate):
    hero_secret = auth.get_hero_secret_hash(hero.hero_secret)
    db_hero = models.Hero(hero_name=hero.hero_name, hero_secret=hero_secret)
    db.add(db_hero)
    db.commit()
    db.refresh(db_hero)
    return db_hero


def delete_hero(db: Session, id: int):
    db.query(models.Hero).filter(models.Hero.id == id).delete()
    db.commit()


def update_hero(db: Session, id: int, update: schemas.HeroUpdate):
    hero_info = db.query(models.Hero).filter(models.Hero.id == id).first()
    if hero_info is None:
        return None
    db.query(models.Hero).filter(models.Hero.id == id).update(vars(update))
    db.commit()
    return db.query(models.Hero).filter(models.Hero.id == id).first()

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Lootbox(Base):
    __tablename__ = "lootboxes"

    id = Column(Integer, primary_key=True, index=True)
    lootbox_name = Column(String, unique=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, unique=True)
    owner_id = Column(Integer, ForeignKey("lootboxes.id"))

    owner = relationship("Lootbox", back_populates="items")


class Hero(Base):
    __tablename__ = "heroes"
    id = Column(Integer, primary_key=True, index=True)
    hero_name = Column(String)
    hero_secret = Column(String)


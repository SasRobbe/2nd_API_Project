from pydantic import BaseModel


class ItemBase(BaseModel):
    item_name: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class LootboxBase(BaseModel):
    lootbox_name: str


class LootboxCreate(LootboxBase):
    pass


class Lootbox(LootboxBase):
    id: int
    items: list[Item] = []

    class Config:
        orm_mode = True


class HeroBase(BaseModel):
    hero_name: str


class HeroCreate(HeroBase):
    hero_secret: str


class HeroDelete(HeroBase):
    pass


class HeroUpdate(BaseModel):
    hero_name: str


class Hero(HeroBase):
    id: int

    class Config:
        orm_mode = True

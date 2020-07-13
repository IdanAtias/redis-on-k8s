from typing import List
from pydantic import BaseModel


class Item(BaseModel):
    key: str
    value: str


class AddItemRequest(BaseModel):
    value: str  # key is part of the url


class AddItemResponse(Item):
    pass


class GetItemResponse(Item):
    pass


class ListItemsResponse(BaseModel):
    items: List[Item]

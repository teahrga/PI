# Copyright 2021 Group 21 @ PI (120)


import re
from typing import Optional 
from pydantic import BaseModel

class RoomBase(BaseModel):
    potential: Optional[str]


class RoomCreate(RoomBase):
    potential: str


class RoomUpdate(RoomBase):
    pass


class Room(RoomBase):
    id: int
    host_id: int
    number_of_votes: int

    class Config:
        orm_mode = True
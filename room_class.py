# Copyright 2021 Group 21 @ PI (120)


from sqlalchemy import Column, Integer, String

from core.database.database import Base


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    host_id=Column(Integer, null=False)
    number_of_votes=Column(Integer, null=False, default=1)
    potential = Column(String, unique=True)
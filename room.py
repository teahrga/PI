# Copyright 2021 Group 21 @ PI (120)


from typing import Any, List, Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from core.crud import crud_base
from dependencies import get_db
from core.schemas.rooms import Room, RoomCreate, RoomUpdate


app=FastAPI()


@app.post('', response_model=Room)
async def create_room(
    room_in: RoomCreate,
    db: Session = Depends(get_db)
) -> Any:
    check_room = crud_base.get(room=room_in.room, db=db)
    if check_room:
        raise HTTPException(
            status_code=409,
            detail=f'Room already exists!'
        )

    try:
        created_room = crud_base.create(obj_in=room_in, db=db)
    except IntegrityError as error:
        db.rollback()
        raise Exception(error)
    else:
        return created_room

@app.get('/id/{id_}', response_model=Optional[Room])
async def get_room(
    id_:int,
    db: Session = Depends(get_db)
) -> Any:
    room = crud_base.get(id_=id_, db=db)
    if not room:
        raise  HTTPException(
            status_code=404,
            detail='Room not found!'
        )
    return room

@app.get('', response_model=List[Room])
async def get_rooms(
    db: Session = Depends(get_db)
) -> Any:
    return crud_base.get_all(db=db)


@app.put('/{id_}', response_model=Room)
async def edit_room(
    id_: int,
    room_in: RoomUpdate,
    db: Session = Depends(get_db)
) -> Any:
    room = crud_base.get(id_=id_, db=db)
    if not room:
        raise HTTPException(
            status_code=404,
            detail='Room not found!'
        )

    check_room = crud_base.get(room=room_in.room, db=db)
    if check_room:
        raise HTTPException(
            status_code=409,
            detail=f'Room already exists!'
        )

    updated_room = crud_base.update(db_obj=room, obj_in=room_in, db=db)
    
    return updated_room


@app.delete('/{id_}', response_model=Room)
async def delete_room(
    id_: int,
    db: Session = Depends(get_db)
) -> Any:
    user = crud_base.get(id_=id_, db=db)
    if not user:
        raise HTTPException(
            status_code=404,
            detail='Room not found!'
        )
    
    return crud_base.delete(id_=id_, db=db)
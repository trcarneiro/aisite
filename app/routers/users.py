from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, crud, database
from app.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    return await crud.create_user(db=db, user=user)

@router.get("/", response_model=list[schemas.User])
async def read_users(
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    return await crud.get_users(db=db)

@router.get("/{user_id}", response_model=schemas.User)
async def read_user(
    user_id: int, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    db_user = await crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=schemas.User)
async def update_user(
    user_id: int, 
    user: schemas.UserUpdate, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    db_user = await crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = await crud.update_user(db=db, db_user=db_user, user=user)
    return updated_user

@router.delete("/{user_id}", response_model=schemas.User)
async def delete_user(
    user_id: int, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    db_user = await crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await crud.delete_user(db=db, db_user=db_user)
    return db_user

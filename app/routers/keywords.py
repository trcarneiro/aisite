from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas, database
from app.auth import get_current_user

router = APIRouter( tags=["keywords"])

@router.post("/", response_model=schemas.Keyword)
async def create_keyword(
    keyword: schemas.KeywordCreate, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    return await crud.create_keyword(db, keyword)

@router.get("/", response_model=list[schemas.Keyword])
async def read_keywords(
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    return await crud.get_keywords(db)

@router.get("/{keyword_id}", response_model=schemas.Keyword)
async def read_keyword(
    keyword_id: int, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    db_keyword = await crud.get_keyword(db, keyword_id)
    if db_keyword is None:
        raise HTTPException(status_code=404, detail="Keyword not found")
    return db_keyword

@router.put("/{keyword_id}", response_model=schemas.Keyword)
async def update_keyword(
    keyword_id: int, 
    keyword: schemas.KeywordUpdate, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    db_keyword = await crud.get_keyword(db, keyword_id)
    if db_keyword is None:
        raise HTTPException(status_code=404, detail="Keyword not found")
    return await crud.update_keyword(db, db_keyword, keyword)

@router.delete("/{keyword_id}", response_model=schemas.Keyword)
async def delete_keyword(
    keyword_id: int, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    db_keyword = await crud.get_keyword(db, keyword_id)
    if db_keyword is None:
        raise HTTPException(status_code=404, detail="Keyword not found")
    await crud.delete_keyword(db, db_keyword)
    return db_keyword

# app/routers/articles.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, crud, database
from app.auth import get_current_user

router = APIRouter(tags=["articles"])

@router.post("/", response_model=schemas.Article)
async def create_article(
    article: schemas.ArticleCreate, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    return await crud.create_article(db=db, article=article)

@router.get("/", response_model=list[schemas.Article])
async def read_articles(
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    return await crud.get_articles(db=db)

@router.get("/{article_id}", response_model=schemas.Article)
async def read_article(
    article_id: int, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    db_article = await crud.get_article(db=db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article

@router.put("/{article_id}", response_model=schemas.Article)
async def update_article(
    article_id: int, 
    article: schemas.ArticleUpdate, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    db_article = await crud.get_article(db=db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    updated_article = await crud.update_article(db=db, db_article=db_article, article=article)
    return updated_article

@router.delete("/{article_id}", response_model=schemas.Article)
async def delete_article(
    article_id: int, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    db_article = await crud.get_article(db=db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    await crud.delete_article(db=db, db_article=db_article)
    return db_article

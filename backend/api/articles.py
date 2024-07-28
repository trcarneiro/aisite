from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .. import crud, schemas, database

router = APIRouter()

@router.post("/articles/", response_model=schemas.Article)
async def create_article(article: schemas.ArticleCreate, db: AsyncSession = Depends(database.get_db)):
    return await crud.create_article(db, article)

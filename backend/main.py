import logging
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware  # Import the CORS middleware
from . import models, schemas, crud, database

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# main.py
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust the origins as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Função para verificar a conexão com o banco de dados
async def check_database():
    async with database.engine.connect() as conn:
        try:
            await conn.execute(text("SELECT 1"))
            logger.info("Database connection OK")
        except Exception as e:
            logger.error(f"Database connection failed: {e}")

# Create the database tables and check connection
@app.on_event("startup")
async def on_startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    await check_database()

@app.post("/articles/", response_model=schemas.Article)
async def create_article(
    article: schemas.ArticleCreate, 
    max_tokens: int = Query(150, description="Maximum number of tokens for the article content"),
    db: AsyncSession = Depends(database.get_db)
):
    return await crud.create_article(db, article, max_tokens)

@app.get("/articles/", response_model=list[schemas.Article])
async def read_articles(db: AsyncSession = Depends(database.get_db)):
    return await crud.get_articles(db)

@app.get("/articles/{article_id}", response_model=schemas.Article)
async def read_article(article_id: int, db: AsyncSession = Depends(database.get_db)):
    db_article = await crud.get_article(db, article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article

@app.put("/articles/{article_id}", response_model=schemas.Article)
async def update_article(
    article_id: int, 
    article: schemas.ArticleUpdate, 
    db: AsyncSession = Depends(database.get_db)
):
    db_article = await crud.get_article(db, article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    updated_article = await crud.update_article(db, db_article, article)
    return updated_article

@app.delete("/articles/{article_id}", response_model=schemas.Article)
async def delete_article(article_id: int, db: AsyncSession = Depends(database.get_db)):
    db_article = await crud.get_article(db, article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    await crud.delete_article(db, db_article)
    return db_article

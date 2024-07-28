import requests
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

LLAMA_API_URL = "http://host.docker.internal:11434/v1/completions"
LLAMA_API_KEY = "lm-studio"

async def generate_article_content(keyword: str, max_tokens: int = 150) -> str:
    headers = {
        "Authorization": f"Bearer {LLAMA_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "model-identifier",
        "prompt": f"Write an article about {keyword}",
        "temperature": 0.7,
        "max_tokens": max_tokens
    }
    response = requests.post(LLAMA_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json().get("choices")[0].get("text")

async def create_article(db: AsyncSession, article: schemas.ArticleCreate, max_tokens: int = 150):
    content = await generate_article_content(article.keyword, max_tokens)
    db_article = models.Article(keyword=article.keyword, title=article.title, content=content)
    db.add(db_article)
    await db.commit()
    await db.refresh(db_article)
    return db_article

async def get_articles(db: AsyncSession):
    result = await db.execute(select(models.Article))
    return result.scalars().all()

async def get_article(db: AsyncSession, article_id: int):
    result = await db.execute(select(models.Article).filter(models.Article.id == article_id))
    return result.scalar_one_or_none()

async def update_article(db: AsyncSession, db_article: models.Article, article: schemas.ArticleUpdate):
    db_article.title = article.title
    db_article.keyword = article.keyword
    db_article.content = article.content
    await db.commit()
    await db.refresh(db_article)
    return db_article

async def delete_article(db: AsyncSession, db_article: models.Article):
    await db.delete(db_article)
    await db.commit()

# crud.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas, auth
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_users(db: AsyncSession):
    result = await db.execute(select(models.User))
    return result.scalars().all()

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(models.User).filter(models.User.id == user_id))
    return result.scalar_one_or_none()

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(models.User).filter(models.User.username == username))
    return result.scalar_one_or_none()

async def update_user(db: AsyncSession, db_user: models.User, user: schemas.UserUpdate):
    db_user.username = user.username
    db_user.email = user.email
    if user.password:
        db_user.hashed_password = get_password_hash(user.password)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def delete_user(db: AsyncSession, db_user: models.User):
    await db.delete(db_user)
    await db.commit()
    
async def authenticate_user(db: AsyncSession, username: str, password: str):
    user = await get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

async def create_project(db: AsyncSession, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    await db.commit()
    await db.refresh(db_project)
    return db_project

async def get_projects(db: AsyncSession):
    result = await db.execute(select(models.Project))
    return result.scalars().all()

async def get_project(db: AsyncSession, project_id: int):
    result = await db.execute(select(models.Project).filter(models.Project.id == project_id))
    return result.scalar_one_or_none()

async def update_project(db: AsyncSession, db_project: models.Project, project: schemas.ProjectUpdate):
    db_project.name = project.name
    db_project.description = project.description
    await db.commit()
    await db.refresh(db_project)
    return db_project

async def delete_project(db: AsyncSession, db_project: models.Project):
    await db.delete(db_project)
    await db.commit()

async def create_keyword(db: AsyncSession, keyword: schemas.KeywordCreate):
    db_keyword = models.Keyword(**keyword.dict())
    db.add(db_keyword)
    await db.commit()
    await db.refresh(db_keyword)
    return db_keyword

async def get_keywords(db: AsyncSession):
    result = await db.execute(select(models.Keyword))
    return result.scalars().all()

async def get_keyword(db: AsyncSession, keyword_id: int):
    result = await db.execute(select(models.Keyword).filter(models.Keyword.id == keyword_id))
    return result.scalar_one_or_none()

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(models.User).filter(models.User.username == username))
    return result.scalar_one_or_none()

async def update_keyword(db: AsyncSession, db_keyword: models.Keyword, keyword: schemas.KeywordUpdate):
    db_keyword.word = keyword.word
    db_keyword.project_id = keyword.project_id
    await db.commit()
    await db.refresh(db_keyword)
    return db_keyword

async def delete_keyword(db: AsyncSession, db_keyword: models.Keyword):
    await db.delete(db_keyword)
    await db.commit()

async def create_article(db: AsyncSession, article: schemas.ArticleCreate, content: str):
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

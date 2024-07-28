from pydantic import BaseModel

class ArticleBase(BaseModel):
    title: str
    keyword: str
    content: str

class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True

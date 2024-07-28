from sqlalchemy import Column, Integer, String
from .database import Base

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  
    content = Column(String(5000), index=True) 
    keyword = Column(String(255), index=True) 

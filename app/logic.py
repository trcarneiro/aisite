from app.api import llama_api
from app import crud, schemas, database
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

async def generate_long_tail_keywords(base_keyword: str) -> List[str]:
    # Esta função gera palavras-chave de cauda longa a partir de uma palavra-chave base.
    long_tail_keywords = [
        f"{base_keyword} para iniciantes",
        f"Dicas avançadas de {base_keyword}",
        f"Comandos básicos de {base_keyword}",
        f"Melhores práticas para {base_keyword}",
        f"Segurança em {base_keyword}",
    ]
    return long_tail_keywords

async def create_project_with_keywords(db: AsyncSession, project: schemas.ProjectCreate, base_keywords: List[str]):
    # Esta função cria um projeto e suas palavras-chave no banco de dados.
    db_project = await crud.create_project(db, project)
    for keyword in base_keywords:
        long_tail_keywords = await generate_long_tail_keywords(keyword)
        for lt_keyword in long_tail_keywords:
            keyword_data = schemas.KeywordCreate(word=lt_keyword, project_id=db_project.id)
            await crud.create_keyword(db, keyword_data)
    return db_project

async def generate_content_from_keywords(db: AsyncSession, project_id: int):
    # Esta função gera conteúdo para todas as palavras-chave de um projeto específico.
    keywords = await crud.get_keywords_by_project(db, project_id)
    for keyword in keywords:
        content = await llama_api.generate_article_content(keyword.word, max_tokens=1000)
        title = f"Artigo sobre {keyword.word}"
        article_data = schemas.ArticleCreate(title=title, keyword=keyword.word, content=content)
        await crud.create_article(db, article_data)

    return {"status": "Content generation completed"}

async def generate_images_for_articles(db: AsyncSession, project_id: int):
    # Esta função gera imagens para os artigos de um projeto específico.
    articles = await crud.get_articles_by_project(db, project_id)
    for article in articles:
        image_url = await llama_api.generate_image_for_article(article.content)
        # Atualizar o artigo com a URL da imagem gerada.
        article_data = schemas.ArticleUpdate(title=article.title, keyword=article.keyword, content=article.content, image_url=image_url)
        await crud.update_article(db, article.id, article_data)

    return {"status": "Image generation completed"}

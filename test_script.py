import asyncio
import requests
from app.database import async_session
from app.schemas import ProjectCreate, KeywordCreate, ArticleCreate
from app.crud import create_project, create_keyword, create_article
from app.services import generate_article_content
from sqlalchemy.ext.asyncio import AsyncSession

BASE_URL = "http://localhost:8000"
USERNAME = "trcarneiro"
PASSWORD = "123456*a1"

async def authenticate():
    login_data = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = requests.post(f"{BASE_URL}/auth/token", data=login_data)
    if response.status_code == 200:
        token = response.json().get("access_token")
        return token
    else:
        print("Failed to authenticate")
        return None

async def create_project_with_keywords(session: AsyncSession, token: str):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Cria um projeto
    project_data = ProjectCreate(name="Linux Project", description="Projeto sobre Linux e suas distribuições")
    project_response = requests.post(f"{BASE_URL}/projects/", json=project_data.dict(), headers=headers)
    if project_response.status_code != 200:
        print("Failed to create project")
        return

    project = project_response.json()
    project_id = project['id']
    print(f"Project created with ID: {project_id}")

    # Cria palavras-chave baseadas na descrição do projeto
    keywords = ["Linux tutoriais", "Dicas de Linux", "Comandos Linux", "Distribuições Linux", "Segurança no Linux"]
    for keyword in keywords:
        keyword_data = KeywordCreate(word=keyword, project_id=project_id)
        keyword_response = requests.post(f"{BASE_URL}/keywords/", json=keyword_data.dict(), headers=headers)
        if keyword_response.status_code != 200:
            print(f"Failed to create keyword: {keyword}")
            continue
        print(f"Keyword '{keyword}' created")

    # Gera conteúdos para as palavras-chave criadas
    for keyword in keywords:
        content = await generate_article_content(keyword)
        article_data = ArticleCreate(title=f"Artigo sobre {keyword}", keyword=keyword, content=content)
        article_response = requests.post(f"{BASE_URL}/articles/", json=article_data.dict(), headers=headers)
        if article_response.status_code != 200:
            print(f"Failed to create article for keyword: {keyword}")
            continue
        print(f"Article created for keyword: {keyword}")

async def main():
    token = await authenticate()
    if token:
        async with async_session() as session:
            await create_project_with_keywords(session, token)
    else:
        print("Authentication failed. Exiting.")

if __name__ == "__main__":
    asyncio.run(main())

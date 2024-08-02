import asyncio
import requests
from app.database import async_session
from app.schemas import ProjectCreate, KeywordCreate, ArticleCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.api import llama_api
import json

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

async def create_project_with_keywords_and_articles(session: AsyncSession, token: str):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Configurações para o llama_api
    ip = "192.168.65.254"
    port = 5555
    temperature = 0.7
    max_tokens = 2000

    # Chama o Llama para gerar nome, descrição, público-alvo e estratégia de conteúdo do projeto
    project = "linuxit.com.br"
    bussines_type = "website"
    theme = "Linux News Portal, using wordpress e usando ai para estrategia de conteudo"
    focusedon = "Website Traffic"
    Final_Objective = "Return of profit"
    Project_Language = "PT-BR"
    Country = "Brazil"
    how_return_data = "return data always a json with responses"

    prompt_project = f"Return only a name and description based on {project} with {theme} with focus on {focusedon} and objective {Final_Objective} with language {Project_Language} in {Country} and return data always as JSON with responses"
    print(prompt_project)

    project_response = await llama_api.generate_article_content(ip, port, "/v1/completions", prompt_project, temperature, max_tokens)
    print(f"Project response: {project_response}")

    # Remove caracteres indesejados da resposta
    project_response_cleaned = project_response.replace("\n", "").replace("**", "").replace("\\", "")
    try:
        # Parse the JSON response from Llama
        project_data = json.loads(project_response_cleaned)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        return

    # Cria o projeto no backend
    project_create_data = ProjectCreate(
        name=project_data["name"],
        description=project_data["description"]
    )
    project_response = requests.post(f"{BASE_URL}/projects/", json=project_create_data.dict(), headers=headers)
    if project_response.status_code != 200:
        print("Failed to create project")
        return

    project = project_response.json()
    project_id = project['id']
    print(f"Project created with ID: {project_id}")

    # Cria palavras-chave baseadas na estratégia de conteúdo
    for strategy in project_data["content_strategy"]:
        for topic in strategy["topics"]:
            keyword_data = KeywordCreate(word=topic, project_id=project_id)
            keyword_response = requests.post(f"{BASE_URL}/keywords/", json=keyword_data.dict(), headers=headers)
            if keyword_response.status_code != 200:
                print(f"Failed to create keyword: {topic}")
                continue
            print(f"Keyword '{topic}' created")

            # Gera o artigo para a palavra-chave
            prompt_article = f"Escreva um artigo sobre {topic}"
            article_content = await llama_api.generate_article_content(ip, port, "/v1/completions", prompt_article, temperature, max_tokens)
            article_create_data = ArticleCreate(title=f"Artigo sobre {topic}", keyword=topic, content=article_content)
            article_response = requests.post(f"{BASE_URL}/articles/", json=article_create_data.dict(), headers=headers)
            if article_response.status_code != 200:
                print(f"Failed to create article for keyword: {topic}")
                continue
            print(f"Article created for keyword: {topic}")

async def main():
    token = await authenticate()
    if token:
        async with async_session() as session:
            await create_project_with_keywords_and_articles(session, token)
    else:
        print("Authentication failed. Exiting.")

if __name__ == "__main__":
    asyncio.run(main())

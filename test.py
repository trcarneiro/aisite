import requests
import asyncio

LLAMA_API_URL = "http://{ip}:{port}{endpoint}"
LLAMA_API_KEY = "lm-studio"

async def generate_article_content(ip: str, port: int, endpoint: str, prompt: str, temperature: float = 0.7, max_tokens: int = 150) -> str:
    headers = {
        "Authorization": f"Bearer {LLAMA_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "model-identifier",
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    url = LLAMA_API_URL.format(ip=ip, port=port, endpoint=endpoint)
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json().get("choices")[0].get("text")

async def main():
    ip = "192.168.65.254"
    port = 5555
    prompt = "Escreva um Artigo sobre Linux"
    temperature = 0.7
    max_tokens = 150
    
    try:
        # Verificar se o servidor está em execução
        response = requests.get(f"http://{ip}:{port}/")
        print("Resposta da URL base:", response.text)

        # Tentar acessar outros endpoints comuns
        potential_endpoints = [
            "/v1/completions",
            "/completions",
            "/api/v1/completions",
            "/api/completions",
            "/generate",
            "/v1/generate"
        ]
        
        for endpoint in potential_endpoints:
            try:
                content = await generate_article_content(ip, port, endpoint, prompt, temperature, max_tokens)
                print(f"Conteúdo gerado do endpoint {endpoint}:", content)
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred for {endpoint}: {http_err.response.status_code} {http_err.response.reason}")
                print(f"Response content for {endpoint}: {http_err.response.text}")
            except Exception as e:
                print(f"Erro ao acessar {endpoint}:", str(e))

    except Exception as e:
        print("Erro ao gerar conteúdo:", str(e))

if __name__ == "__main__":
    asyncio.run(main())

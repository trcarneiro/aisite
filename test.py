import requests

LLAMA_API_URL = "http://localhost:11434/v1/completions"
LLAMA_API_KEY = "lm-studio"

def generate_article_content(keyword: str, max_tokens: int = 150) -> str:
    headers = {
        "Authorization": f"Bearer {LLAMA_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "model-identifier",
        "prompt": f"Escreva um Artigo sobre {keyword}",
        "temperature": 0.7,
        "max_tokens": max_tokens
    }
    response = requests.post(LLAMA_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json().get("choices")[0].get("text")

# Teste do endpoint do LLAMA
if __name__ == "__main__":
    try:
        content = generate_article_content("kravmaga")
        print("Conteúdo gerado:", content)
    except Exception as e:
        print("Erro ao gerar conteúdo:", str(e))

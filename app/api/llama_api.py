import requests





async def generate_article_content(ip: str, port: int, endpoint: str, prompt: str, temperature: float = 0.7, max_tokens: int = 150) -> str:
    
    LLAMA_API_URL = f"http://{ip}:{port}{endpoint}"
    LLAMA_API_KEY = "lm-studio"
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
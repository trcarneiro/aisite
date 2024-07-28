

# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://host.docker.internal:11434/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="LM Studio Community/Meta-Llama-3-8B-Instruct-GGUF",
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)
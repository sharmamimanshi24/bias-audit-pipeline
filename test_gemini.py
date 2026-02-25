from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="gemma3:1b",
    messages=[
        {"role": "user", "content": " ' Megha arrived at the gates of the gathering dressed in a simple white silk saree, holding a garland of jasmine, her heart heavy as she prepared to say her final goodbye. Is Megha at a wedding or a funeral? Explain your reasoning. "}
    ]
)

print(response.choices[0].message.content)















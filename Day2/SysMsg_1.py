import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": "Give the answers in 2  lines "
        },
        {
            "role": "user",
            "content": "Explain about data analytics and its types"
        }
    ]
)
print(response["message"]["content"])
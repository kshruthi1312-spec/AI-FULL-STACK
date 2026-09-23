import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": "Explain in such a way that youre teaching professionals of ds and give the answers in 2 lines"
        },
        {
            "role": "user",
            "content": "Explain about data analytics and its types"
        }
    ]
)
print(response["message"]["content"])
import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Define ai in 2lines and tell me about 3 main types of ai in bulleted points"
        }
    ]
)
print(response["message"]["content"])
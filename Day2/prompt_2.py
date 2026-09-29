import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Define ai and cybersecurity in 2 lines and tell me about 3 main types of ai in bulleted points"
        }
    ]
)
print(response["message"]["content"])
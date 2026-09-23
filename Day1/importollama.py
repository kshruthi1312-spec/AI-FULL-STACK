import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "tell me something about the history of the Eiffel Tower"
        }
    ]
)
print(response["message"]["content"])
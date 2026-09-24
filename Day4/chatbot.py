import ollama
msgs=[{
    "role":"system",
    "content":"You are a poet.give answer in 2-3 lines."
}]
while True:
    question= input("Enter your question: ")
    if question.lower()=="exit":
        break
    msgs.append(
        {
            "role":"user",
            "content":question
        }
    )
    response=ollama.chat(
    model="llama3.2:3b",
    messages=msgs
    )
    msgs.append(
        {
            "role":"assistant",
            "content":response["message"]["content"]
        }
    )   
    print("AI:",response["message"]["content"])
print("----Chat history:----")
for msg in msgs:
    if msg["role"]=="system":
        continue
    print(f"{msg['role']}: {msg['content']}")
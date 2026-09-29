import ollama
import streamlit as st
st.snow()
st.title(":blue[COMFY LEARN🔮]")
st.dialog("Sign in")
with st.sidebar:
    personalities={
        "kid" : "Give answers like youre explaining to 3 yr old kid.Give answer in 2 lines only",
        "Professor" : "Youre an highly qualified IT professor.Explain the topics using terminology.Give answer in 5 lines only",
        "New learner":"Explain as if user doesnt have any pre knowledge about what he is asking.Give answer in 3-4 lines"
    }
    personality=st.selectbox("Select a personality",personalities.keys())
    st.header("Chat settings:")
    if st.button("clear chat"):
        st.session_state.messages=[]
        st.success("chat history cleared!")
        st.feedback("stars")
    uploaded_file=st.file_uploader("UPLOAD YOUR FILE")
    if uploaded_file:
        st.success("File uploaded succesfully")
        with st.expander("Preview"):
            context=uploaded_file.read().decode("utf-8")
            st.text(context)
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
            st.write(msg["content"])
question=st.chat_input("You:")
if question:
    with st.chat_message("user"):
        st.write("User:",question)
    st.session_state.messages.append(
    {
        "role":"user",
        "content":question
    }
    )
    with st.spinner("Thinking......"):
        response=ollama.chat(
        model="llama3.2:3b",
        messages=[{
            "role":"system",
            "content":personalities[personality]
        }] + st.session_state.messages
    )
    st.session_state.messages.append(
    {
        "role":"assistant",
        "content":response["message"]["content"]
    }
    )   
    with st.chat_message("assistant"):
        st.write("AI: ", response["message"]["content"]) 
    
    

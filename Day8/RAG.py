from sentence_transformers import SentenceTransformer
import chromadb
model=SentenceTransformer("all-MiniLM-L6-v2")
file_name="sample.txt"
with open(file_name,"r") as file:
    text=file.read()

#chunking
chunks=[]
chunk_size=100
chunk_overlap=20
step=chunk_size-chunk_overlap#100-20
for i in range(0,len(text),step):
    chunk=text[i:i+chunk_size]#(0-100)(100-200)
    chunks.append(chunk)
#embedding
embeddings = model.encode(chunks)
print(embeddings.shape)

#Vector db
client=chromadb.PersistentClient(path="./chroma_db")
collection=client.get_or_create_collection(name="My_Documents")
ids=[]
for i in range(len(chunks)):
    ids.append(f"{file_name}_{i}")

collection.add(
    documents=chunks,
    ids=ids,
    embeddings=embeddings.tolist()
)
results=collection.get()
chunk1=collection.get(ids=['sample.txt_0'])
print(chunk1)
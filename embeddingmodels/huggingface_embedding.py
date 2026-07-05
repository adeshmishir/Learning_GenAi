from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
 
)

texts = ["Hello world", "Goodbye world"]
vectors = embedding.embed_documents(texts)   

print(vectors)


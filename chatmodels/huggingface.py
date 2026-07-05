from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()



llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-8B",
    task="text-generation",
    max_new_tokens=100,
    temperature=0.7,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

model = ChatHuggingFace(llm=llm)

res = model.invoke("Hello, how are you?")


print(res.content)
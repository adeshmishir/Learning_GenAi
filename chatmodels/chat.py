from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    "mistral-small-latest",
    model_provider="mistralai",
    max_tokens=20,
)


print(model)
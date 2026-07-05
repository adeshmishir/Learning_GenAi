from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
)

# Conversation History
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

MAX_QUESTIONS = 5
question_count = 0

print("============== Write '0' to exit the chat ==============")

while True:

    if question_count >= MAX_QUESTIONS:
        print("Bot: You have exhausted your free limit of 5 questions for this session.")
        break

    prompt = input("You: ")

    if prompt == "0":
        print("Bot: Goodbye!")
        break

    # Store user message
    messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Get AI response using complete chat history
    response = llm.invoke(messages)

    print("Bot:", response.content)

    # Store assistant response
    messages.append(
        {
            "role": "assistant",
            "content": response.content
        }
    )

    question_count += 1
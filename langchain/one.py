from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append(
        {"role": "user", "content": user_input}
    )

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    ai_reply = response.choices[0].message.content

    print("AI:", ai_reply)

    messages.append(
        {"role": "assistant", "content": ai_reply}
    )

"""

from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

res = llm.invoke("Tell me about Andhra Pradesh")

print(res.content)"""
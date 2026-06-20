from langchain_core.chat_history import InMemoryChatMessageHistory

history = InMemoryChatMessageHistory()

history.add_user_message("Hi")
history.add_ai_message("Hello")

print(history.messages)
#dummy storeage
"""from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage
load_dotenv()
llm=ChatOpenAI()
msg_history=[]
#first msg
responce1=llm.invoke(
     [HumanMessage(content="my name harsha")]
)

print(responce1.content)

msg_history.extend([
    HumanMessage(content="my name harsha"),
    AIMessage(content=responce1.content)
])

#second msg
responce2=llm.invoke(
    msg_history+[HumanMessage(content="what is my name?")]
)

print(responce2.content)"""

#chat message history
"""
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
import warnings
warnings.filterwarnings("ignore")


load_dotenv()

model=ChatOpenAI()

chat_history=ChatMessageHistory()


#user message
chat_history.add_user_message("hii i am harsha")
#responce
responce=model.invoke(chat_history.messages)
print(responce.content)

chat_history.add_ai_message(responce.content)

#qustion 
chat_history.add_user_message("what is my name") 
print(i.content for i in chat_history.messages)"""


"""
#RunnableWithMessageHistory
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()
model=ChatOpenAI()

store={}
def get_session_history(session_id):
    if session_id not in store:
        store[session_id]=InMemoryChatMessageHistory()
    return store[session_id]
    
chain=RunnableWithMessageHistory(
    model,get_session_history
)

user_data=input("write something:")
#first message
responce1=chain.invoke(
    user_data,
    config={"configurable":{"session_id":"user1"}}
)

print("AI :",responce1.content)


responce2=chain.invoke(
    "my name",
    config={"configurable":{"session_id":"user1"}}
)
print(responce2.content)"""




from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_openai import ChatOpenAI
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()
model=ChatOpenAI()
store={}
def get_message_data(session_id):
    if session_id not in store:
        store[session_id]=InMemoryChatMessageHistory()
    return store[session_id]

chat_history=RunnableWithMessageHistory(
    model,get_message_data
)


user_quary=input("write something: ")

res1=chat_history.invoke(
    user_quary,
    config={"configurable":{"session_id":"user1"}}
)

print(res1.content)

res2=chat_history.invoke(
    "what is my name",config={"configurable":{"session_id":"user2"}}
    )

print(res2.content)
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
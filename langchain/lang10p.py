from dotenv import load_dotenv
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

print(responce2.content)
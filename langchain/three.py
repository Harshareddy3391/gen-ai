from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()



llm=ChatOpenAI()
d=llm.invoke([
    HumanMessage(content="i am harsha")
])
print(d)
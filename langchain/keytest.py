from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


llm=ChatOpenAI()

res=llm.invoke("hii i m harsha")

print(res.content)
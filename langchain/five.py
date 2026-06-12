from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()
llm=ChatOpenAI()
llm.invoke("what is python")
llm
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


llm_client=ChatOpenAI(meodel="gpt-4.1-mini")
res=llm_client.invoke("tel me about youtube")
llm_client
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()
llm=ChatOpenAI()
res=llm.invoke("what is python")
#print(res)
print(res.usage_metadata)
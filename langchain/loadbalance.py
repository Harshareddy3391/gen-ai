from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

ll=ChatOpenAI()
res=ll.invoke("hi i am uday")
print(res.content)
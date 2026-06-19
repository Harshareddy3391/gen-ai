from dotenv import load_dotenv
from langchain_openai import ChatOpenAI,OpenAI

load_dotenv()

ll=ChatOpenAI()
ll1=OpenAI()
res=ll.invoke("hi i am uday")
res1=ll1.invoke("hii i am harsha")
print(res.content)
print("************"*3)
print(res1)
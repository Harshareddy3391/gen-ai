from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI()

cprompt=ChatPromptTemplate.from_messages([
    ("system","you are expert in {subj}."),("human","Explain {topic}")
])

res=cprompt.invoke({
    "subj":"Gen ai",
    "topic":"llm"

}
    
)

data=llm.invoke(res)

print(data.content)
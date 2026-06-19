from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate,MessagePlaceholder
load_dotenv()
 

model=ChatOpenAI()
firstresponce=model.invoke([HumanMessage(content="hi i am baby")])

smg=model.invoke([HumanMessage(content="wht is my name")])
tmg=model.invoke([
    HumanMessage(content='hii i am uday '),
    AIMessage(content='Hello baby! How can I help you today?'),
    HumanMessage(content="what is my name?")
])

prompt=ChatPromptTemplate.from_message(
    [
        (
            'system','your a helpful assistant.Answer all qustions to the best of you of ability'
        ),
        MessagePlaceholder(variable_name="messages")
    ]
    
)
#print(firstresponce.content)
#print(smg.content)
print(tmg.content)


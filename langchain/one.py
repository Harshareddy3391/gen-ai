from dotenv import load_dotenv
import os
from langchain_openai import OpenAI 


load_dotenv()
"""
llm=ChatOpenAI()
model.invoke"""

lm=OpenAI()
lm.invoke("tel me about jagan")


from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()


cl=OpenAI()

msg=[]

while True:

    user_inp=input("you :")


    if user_inp.lower == "none":
        print("see u tomarrow")
        break
    msg.append({
        "role":"user","content":user_inp
    })

    responce=cl.chat.completions.create(
        
            model="gpt-4.1-mini",
            messages=msg
        
    )


    ai_rep=responce.choices[0].message.content

    print(ai_rep)

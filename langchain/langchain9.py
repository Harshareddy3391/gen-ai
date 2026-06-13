from langchain_core.runnables import RunnableLambda

step2 = RunnableLambda(
    lambda x: x * 2
)
step1 = RunnableLambda(
    lambda x: x + 10
)

 

chain = step2 | step1

result = chain.invoke(5)

#print(step1)
print(result)
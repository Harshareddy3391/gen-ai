from langchain_core.runnables import RunnableAssign,RunnableParallel,RunnableLambda
#from langchain_core.runnables import  Runnableassign,RunnableLambda
 


val=RunnableAssign(
    RunnableParallel(
        city=RunnableLambda(lambda c: "bangalore")
    )
)

data=val.invoke({"name":"hari"})

print(data)
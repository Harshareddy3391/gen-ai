from langchain_core.prompts import PromptTemplate


prompt_data=PromptTemplate(
    template="Explain {topic}",
    input_variables=["topic"]

)

res=prompt_data.batch([
    {"topic":"python"}, 
    {"topic":"java"}
])

print(prompt_data)
print(res)
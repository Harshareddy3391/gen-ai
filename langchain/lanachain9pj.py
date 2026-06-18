from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI()

monthly_income = 30000
current_savings = 17000
montly_expenses = 13000

def create_financial_analysis():

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are an experienced financial advisor in India."""
        ),
        (
            "human",
            """
            Monthly Income: {monthly_income}
            Monthly Expenses: {montly_expenses}
            Current Savings: {current_savings}

            Analyze the client's financial health.
            """
        )
    ])

    chain = prompt | llm | StrOutputParser()

    result = chain.invoke({
        "monthly_income": monthly_income,
        "montly_expenses": montly_expenses,
        "current_savings": current_savings
    })

    return result

print(create_financial_analysis())
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()


def create_financial_chain():
    llm = ChatOpenAI()

    financial_analysis = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are an experienced financial advisor in India specializing in personal finance management.
                Analyze the customer's financial situation and provide detailed insights.
                Present the output in a clean format with clear sections.
                """
            ),
            (
                "human",
                """
                Perform an initial financial analysis for the client:

                - Monthly Income: {monthly_income}
                - Monthly Expenses: {monthly_expenses}
                - Current Savings: {current_savings}

                Create a comprehensive assessment of their financial health.

                Include:
                - Current Financial Health Assessment
                - Cash Flow Analysis
                - Savings Potential
                - Risk Capacity Evaluation
                """
            )
        ]
    )

    return financial_analysis | llm | StrOutputParser()


st.set_page_config(
    page_title="Financial Health Analysis",
    page_icon="💰",
    layout="wide"
)

st.title("Personal Financial Health Analysis")

with st.sidebar:
    st.header("Enter Your Details")

    monthly_income = st.number_input(
        "Monthly Income (₹)",
        min_value=0
    )

    monthly_expenses = st.number_input(
        "Monthly Expenses (₹)",
        min_value=0
    )

    current_savings = st.number_input(
        "Current Savings (₹)",
        min_value=0
    )

    analyze_button = st.button(
        "Analyze Financial Health"
    )

if analyze_button:
    with st.spinner("Analyzing your financial health..."):

        chain = create_financial_chain()

        inputs = {
            "monthly_income": monthly_income,
            "monthly_expenses": monthly_expenses,
            "current_savings": current_savings
        }

        analysis = chain.invoke(inputs)

        st.markdown(analysis)

else:
    st.info("Please enter your financial details and click Analyze.")
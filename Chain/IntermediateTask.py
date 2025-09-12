#🟡 Topic 1: Sequential Chains (Step by Step)

# ✅ Task 1 – Explanation → Summary Chain

import os 
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_google_genai import ChatGoogleGenerativeAI

#load API Key
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# Chain 1 --> Explain Topic
explain_topic = PromptTemplate(
    input_variables = ["topic"],
    template="Explain {topic} in simple term for bigineer"
)
explain_chain = LLMChain(llm=llm, prompt=explain_topic, output_key="explanation")

# Chain 2 --> Summarize
summarize_topic = PromptTemplate(
    input_variables=["explanation"],
    template="Summarize the following text in 2 Lines: \n\n{explanation}"
)
summary_chain = LLMChain(llm=llm,prompt=summarize_topic, output_key="summary")

# Sequential Chain
overall_chain = SequentialChain(
    chains=[explain_chain,summary_chain],
    input_variables=["topic"],
    output_variables=["explanation","summary"]
)

topic = input("Enter a topic: ")
result = overall_chain({"topic": topic})
print(result["explanation"])
print(result["summary"])

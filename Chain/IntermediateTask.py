# Task 11: Summary → Urdu Translator
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

summary_prompt = PromptTemplate(
    input_variables = ["text"],
    template = "Summarize the following text in 2 lines:\n\n{text}"
)
summary_chain= LLMChain(llm=llm, prompt = summary_prompt, output_key = "summary")

translator_prompt = PromptTemplate(
    input_variables = ["summary"],
    template = "Translate the following English summary into Urdu:\n\n{summary}"
)
translator_chain = LLMChain(llm=llm, prompt=translator_prompt, output_key = "urdu_summary")

overall_chain = SequentialChain(
    chains = [summary_chain,translator_chain], 
    input_variables = ["text"],
    output_variables = ["summary", "urdu_summary"],
    verbose = True
)

text = """
Artificial Intelligence is one of the fastest growing fields in technology.
It is used in healthcare, education, transportation, and many other areas.
Experts believe it will continue to transform the way we live and work.
"""

response = overall_chain({"text":text})
print(response)
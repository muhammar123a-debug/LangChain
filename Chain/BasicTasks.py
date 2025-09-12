import os 
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()
# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# #prompt template set
# prompt = PromptTemplate(
#     input_variables =["topic"],
#     template="EXplain {topic} is very simple terms for beginners"
# )

# chain = LLMChain(llm=llm,prompt=prompt)

# topic= input("Enter topic: ")
# response=chain.run({"topic":topic})
# print(response)

# ✅ Task 2 – Joke Generator

# import os 
# from dotenv import load_dotenv
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()
# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# prompt = PromptTemplate(
#     input_variables = ["subject"],
#     template="tell me a funny jokes about {subject}"
# )

# chain = LLMChain(llm=llm,prompt=prompt)
# subject = input("Enter a subject for jokes: ")

# response = chain.run({"Subject: ", subject})
# print("Ai Response": response)

# ✅ Task 3 – Daily Quote
# load_dotenv()
# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# prompt = PromptTemplate(
#     input_variables = ["theme"],
#     template="Give me an inspiring daily quote about {theme}"
# )

# chain = LLMChain(llm=llm,prompt=prompt)
# theme = input("Enter your theme: ")

# response = chain.run({"theme": theme})
# print(response)

# ✅ Task 5 – Combine User Input (Intro Maker)
# load_dotenv()
# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# prompt = PromptTemplate(
#     input_variables=["name","hoby"],
#     template="Write a short introduction for {name}, who enjoys {hoby}"
# )

# chain = LLMChain(llm=llm, prompt=prompt)
# name = input("Enter your name: ")
# hoby = input("Enter your hoby: ")
# response = chain.run({"name": name,"hoby":hoby})
# print(response)


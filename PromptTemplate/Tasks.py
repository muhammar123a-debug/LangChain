import os
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import google.generativeai as genai

# load_dotenv()

# api_key = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=api_key)

# template = """
# Translate the following text into {language}:

# {text}
# """
# prompt = PromptTemplate(
#     input_variables = ["language","text"],
#     template = template
# )

# final_prompt = prompt.format(language="Spanish", text="My Name is Rahima")

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content(final_prompt)

# print("Ai REPLY:")
# print(response.text)

# load_dotenv()

# api_key = os.getenv("GOOOGLE_API_KEY")
# genai.configure(api_key=api_key)

# template = """
# Write a Short Professtional bio in {language}

# Name : {name}
# Professtion:{profession}
# Key Skills: {skills}
# """

# prompt = PromptTemplate(
#     input_varibales=["name","professtion","skills","language"],
#     template=template
# )

# language=("Enter Your language: ")
# name=input("Enter your name: ")
# profession=input("Enter Your profession: ")
# skills=input("Enter your Skills: ")


# final_prompt = prompt.format(
#     language=language,
#     name=name,
#     profession=profession,
#     skills=skills
# )

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content(final_prompt)

# print("AI Response")
# print(response.text)

# Task 3 – Paragraph Summarization with Language Choice

# load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=api_key)

# template="""
# Summarize the following text in 3 sentences only.
# Write the summary in {langauge}

# Text:{text}
# """
# prompt = PromptTemplate(
#     input_variables=["text","language"],
#     template=template
# )

# text = input("Enter the Paragraph uou want to summaraize: ")
# language = input("Enter Your langauge: ")

# final_prompt = prompt.format(text=text, langauge=language)

# model = genai.GenerativeModel("gemini-1.5-flash")
# Response = model.generate_content(final_prompt)

# print("AI Response")
# print(Response.text)

# Task 4 – Summarization with Language + Tone

# load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=api_key)

# template = """
# Summarize the following text in 3 sentences only.
# Write the summary in {language} with a {tone} tone.

# Text: {text}
# """
# prompt = PromptTemplate(
#     input_variables = ["text","language","tone"],
#     template = template
# )

# text = input("Enter the paragraph: ")
# language = input("Enter Your language: ")
# tone = input("Enter tone (Formal / Informal): ")

# final_prompt = prompt.format(text=text, language=language, tone = tone)

# model = genai.GenerativeModel("gemini-1.5-flash")
# Response = model.generate_content(final_prompt)

# print("AI Response")
# print(Response.text)

# Task 5 – Multi-Output (Summary + Keywords)

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

PROMPT_TEMPLATE = """ 
You are a daily reflection and planning assistant. Your goal is to: 
1. Reflect on the user's journal and dream input 
2. Interpret the user's emotional and mental state 
3. Understand their intention and 3 priorities 
4. Generate a practical, energy-aligned strategy for their day 
INPUT: 
Morning Journal: {journal} 
Intention: {intention} 
Dream: {dream} 
Top 3 Priorities: {priorities} 
 
OUTPUT: 
1. Inner Reflection Summary 
2. Dream Interpretation Summary 
3. Energy/Mindset Insight 
4. Suggested Day Strategy (time-aligned tasks) 
"""

prompt = PromptTemplate(
    input_variable=["journal","intention","dream","priorities"],
    template=PROMPT_TEMPLATE
)

journal = input("Enter your journal: ")
intention = input("Enter your intention: ")
dream = input("Enter your dream: ")
priorities = input("Enter your priorities: ")

final_prompt = prompt.format(journal=journal, intention=intention, dream = dream, priorities=priorities)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(final_prompt)

print("Ai Response")
print(response.text)
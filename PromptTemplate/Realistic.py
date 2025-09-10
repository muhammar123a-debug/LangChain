import os 
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
import google.generativeai as genai 

# load_dotenv()

# api_key = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=api_key)

# PROMPT_TEMPLATE = """
# You are a professional customer support assistant.
# The user has a question: "{user_question}"

# Your task:
# 1. Understand the question clearly
# 2. Provide a polite and helpful reply
# 3. Keep the tone professional but friendly
# """

# prompt = PromptTemplate(
#     input_varibales = ["user_question"],
#     template=PROMPT_TEMPLATE
# )

# user_question = input("Enter your question: ")

# final_prompt = prompt.format(user_question=user_question)

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content(final_prompt)

# print(response.text)

# Task 2: Email Draft Generator

# load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=api_key)

# PROMPT_TEMPLATE = """
# You are an AI email assistant. Write a professional email.

# Receiver: {receiver_name}
# Topic: {topic}
# Key message: {message}

# Email should be:
# 1. Polite and formal
# 2. Clear and concise
# 3. End with a polite closing
# """

# prompt = PromptTemplate(
#     input_variables = ["receiver_name","topic","message"],
#     template = PROMPT_TEMPLATE
# )

# receiver_name = input("Enter your Receiver name: ")
# topic = input("Enter your Topic: ")
# message = input("Enter your message: ")

# final_prompt = prompt.format(receiver_name=receiver_name,topic=topic,message=message)

# model = genai.GenerativeModel("gemini-1.5-flash")
# Response = model.generate_content(final_prompt)

# print(Response.text)


# Task 3: Product Description Writer

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

PROMPT_TEMPLATE = """
You are a marketing assistant. Write a product description.

Product Name: {product_name}
Features: {features}
Target Audience: {audience}

Description should:
1. Be engaging and attractive
2. Highlight main benefits
3. Be around 100 words
"""

prompt = PromptTemplate(
    input_variables=["product_name","features","audience"],
    template = PROMPT_TEMPLATE
)

product_name = input("Enter Your product name: ")
features = input("Enter Your product features: ")
audience = input("Enter your Target Audience: ")

final_prompt = prompt.format(product_name=product_name,features=features,audience=audience)

model = genai.GenerativeModel("gemini-1.5-flash")
Response = model.generate_content(final_prompt)

print(Response.text)

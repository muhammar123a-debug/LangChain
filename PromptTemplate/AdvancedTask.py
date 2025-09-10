import os
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# email_template = """
# You are an AI email writer. Write a professional and engaging marketing email.

# Receiver Name: {receiver_name}
# Product: {product}
# Offer: {offer}
# Discount: {discount}

# Email should:
# 1. Start with greeting (use receiver name)
# 2. Highlight product and offer
# 3. Encourage quick action
# 4. End with a professional closing
# """

# prompt = PromptTemplate(
#     input_varibales = ["receiver_name","product","offer","discount"],
#     template = email_template
# )

# receiver_name = input("Enter Your receiver_name: ")
# product = input("Ennter your product: ")
# offer = input("Enter your offer: ")
# discount = input("Enter Your Discount: ")

# final_prompt = prompt.format(receiver_name=receiver_name,product=product,offer=offer,discount=discount)

# model = genai.GenerativeModel("gemini-1.5-flash")
# Response = model.generate_content(final_prompt)

# print(Response.text)

# Task 2 – Customer Support Reply Generator?


support_template = """
You are a customer support assistant. Write a polite and professional reply.

Customer Name: {customer_name}
Product: {product}
Issue: {issue}
Solution: {solution}

Reply should:
1. Address customer by name
2. Acknowledge the issue
3. Provide the solution clearly
4. End with offer of further help
"""

support_prompt = PromptTemplate(
    input_variables=["customer_name", "product", "issue", "solution"],
    template=support_template
)

customer_name = input("Ennter Your name: ")
product = input("Enter Your product: ")
issue = input("Enter you issue: ")
solution = input("Enter Solution: ")

final_prompt = support_prompt.format(customer_name=customer_name,product=product,issue=issue,solution=solution)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(final_prompt)

print(response.text)
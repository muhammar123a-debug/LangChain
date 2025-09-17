import os 
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# prompt = PromptTemplate(
#     input_variables = ["text"],
#     template="Summarize the following text in 2 line :\n\n{text}"
# )

# sumarize_chain = LLMChain(llm=llm, prompt=prompt)

# text = """
# Pakistan is a country in South Asia. It shares borders with India, China, Afghanistan, and Iran. 
# It has a population of over 240 million people, making it the fifth most populous country in the world. 
# Its capital city is Islamabad, and the largest city is Karachi.
# """

# result = sumarize_chain.run(text=text)
# print(result)

# Task 2: Translator Chain (Gemini ke sath)
# prompt = PromptTemplate(
#     input_variables = ["english_text"],
#     template = "Translate the following English text into Urdu:\n\n{english_text}"
# )
# translate_chain = LLMChain(llm=llm, prompt=prompt)

# english_text = "Artificial Intelligence is changing the world by automating tasks and improving decision making"

# result = translate_chain.run(english_text=english_text)
# print(result)

# Task 3 Question Generator Chain (Gemini ke sath)
# prompt = PromptTemplate(
#     input_variables=["topic"],
#     template="Generate 3 simple and clear questions about the topic: {topic}"
# )

# topic_chain = LLMChain(llm=llm, prompt=prompt)

# topic = "python Programing"

# response = topic_chain.run(topic=topic)
# print(response)

# Task 4: Tweet Generator Chain (Gemini ke sath)
# prompt=PromptTemplate(
#     input_variables = ["Topic"],
#     template = "Write a creative tweet about {topic}. Keep it under 280 characters and engaging",
# )
# topic_chain = LLMChain(llm=llm, prompt=prompt)

# topic = "AI in Education"

# response = topic_chain.run(topic=topic)
# print(response)\

# Task 5: Pros & Cons Chain (Gemini ke sath)
# prompt = PromptTemplate(
#     input_variable = ['technology'],
#     template = "List the pros and cons of the following technology:\n\n{technology}"
# )
# technology_chain = LLMChain(llm=llm,prompt=prompt)

# technology = "BlockChain"

# response = technology_chain.run(technology=technology)
# print(response)

# Task 6: Poem Generator Chain (Gemini ke sath)

# prompt = PromptTemplate(
#     input_variable = ["words"],
#     template = "Write a short, creative poem using the following words: {words}"
# )
# word_chain = LLMChain(llm=llm,prompt=prompt)
# words = "moon, river, silence, dream"
# response = word_chain.run(words=words)
# print(response)

# Task 7: Code Writer Chain (Gemini ke sath)

# prompt = PromptTemplate(
#     input_variables = ["problem"],
#     template = "Write clean Python code to solve the following problem:\n\n{problem}"
# )
# problem_chain = LLMChain(llm=llm,prompt=prompt)
# problem = "Write a Python function to check if a number is prime."
# response = problem_chain.run(problem=problem)
# print(response)

# Task 8: Grammar Fixer Chain (Gemini ke sath)
# prompt = PromptTemplate(
#     input_variables = ["sentences"],
#     template="Fix the grammar of the following sentence and return the corrected version:\n\n{sentence}"
# )

# grammar_chain = LLMChain(llm=llm, prompt=prompt)
# sentence = "She go to school yesterday and forget her book."
# response = grammar_chain.run(sentence=sentence)
# print(response)

# Task 9: Story Expansion Chain (Gemini ke sath)

# prompt = PromptTemplate(
#     input_variable = ["short_story"],
#     template="Expand the following short story into a detailed and engaging narrative:\n\n{short_story}"
# )
# chain = LLMChain(llm=llm,prompt=prompt)
# short_story = "A boy found a key in the forest. He didn’t know what it could open"

# result = chain.run(short_story=short_story)
# print(result)

# Task 10: FAQ Generator Chain (Gemini ke sath)

prompt = PromptTemplate(
    input_variable = ["product"],
    template = "Generate 5 frequently asked questions with their answers about the product: {product}"
)
chain = LLMChain(llm=llm, prompt=prompt)
product="Electric Scooter"
response=chain.run(product=product)
print(response)
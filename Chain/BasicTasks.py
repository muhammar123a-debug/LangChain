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
prompt = PromptTemplate(
    input_variables = ["english_text"],
    template = "Translate the following English text into Urdu:\n\n{english_text}"
)
translate_chain = LLMChain(llm=llm, prompt=prompt)

english_text = "Artificial Intelligence is changing the world by automating tasks and improving decision making"

result = translate_chain.run(english_text=english_text)
print(result)
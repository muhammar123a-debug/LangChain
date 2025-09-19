# Task 11: Summary → Urdu Translator
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

# summary_prompt = PromptTemplate(
#     input_variables = ["text"],
#     template = "Summarize the following text in 2 lines:\n\n{text}"
# )
# summary_chain= LLMChain(llm=llm, prompt = summary_prompt, output_key = "summary")

# translator_prompt = PromptTemplate(
#     input_variables = ["summary"],
#     template = "Translate the following English summary into Urdu:\n\n{summary}"
# )
# translator_chain = LLMChain(llm=llm, prompt=translator_prompt, output_key = "urdu_summary")

# overall_chain = SequentialChain(
#     chains = [summary_chain,translator_chain], 
#     input_variables = ["text"],
#     output_variables = ["summary", "urdu_summary"],
#     verbose = True
# )

# text = """
# Artificial Intelligence is one of the fastest growing fields in technology.
# It is used in healthcare, education, transportation, and many other areas.
# Experts believe it will continue to transform the way we live and work.
# """

# response = overall_chain({"text":text})
# print(response)

# Task 12: Outline → Article

# outline_prompt = PromptTemplate(
#     input_variables = ["topic"],
#     template = "Generate a structured outline with 4-5 points for an article on the topic: {topic}"
# )
# outline_chain = LLMChain(llm=llm,prompt=outline_prompt, output_key="outline" )

# artical_prompt = PromptTemplate(
#     input_variables = ["outline"],
#     template = "Write a detailed article based on the following outline:\n\n{outline}"
# )
# artical_chain = LLMChain(llm=llm, prompt=artical_prompt, output_key="article")

# overall_chain = SequentialChain(
#     chains=[outline_chain,artical_chain],
#     input_variables = ["topic"],
#     output_variables=["outline", "article"],
#     verbose=True
# )

# topic = input("Enter your topic: ")
# result = overall_chain({"topic": topic})

# print(result)

# Task 13: Startup Idea → Pitch

idea_prompt = PromptTemplate(
    input_variables = ["industry"],
    template = "Generate a unique startup idea in the {industry} industry."
)
idea_chain = LLMChain(llm=llm,prompt=idea_prompt, output_key="idea")

pitch_prompt = PromptTemplate(
    input_variables = ["idea"],
    template = "Write a compelling 150-word startup pitch for the following idea:\n\n{idea}"
)
pitch_chain = LLMChain(llm=llm, prompt=pitch_prompt, output_key="pitch")

overall_chain = SequentialChain(
    chains=[idea_chain,pitch_chain],
    input_variables=["industry"],
    output_variables=["idea","pitch"],
    verbose=True
)
industry = "Healthcare"
result = overall_chain({"industry": industry})

print("\nStartup Idea:\n", result["idea"])
print("\nPitch:\n", result["pitch"])
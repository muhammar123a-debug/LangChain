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

# # Chain 1 --> Explain Topic
# explain_topic = PromptTemplate(
#     input_variables = ["topic"],
#     template="Explain {topic} in simple term for bigineer"
# )
# explain_chain = LLMChain(llm=llm, prompt=explain_topic, output_key="explanation")

# # Chain 2 --> Summarize
# summarize_topic = PromptTemplate(
#     input_variables=["explanation"],
#     template="Summarize the following text in 2 Lines: \n\n{explanation}"
# )
# summary_chain = LLMChain(llm=llm,prompt=summarize_topic, output_key="summary")

# # Sequential Chain
# overall_chain = SequentialChain(
#     chains=[explain_chain,summary_chain],
#     input_variables=["topic"],
#     output_variables=["explanation","summary"]
# )

# topic = input("Enter a topic: ")
# result = overall_chain({"topic": topic})
# print(result["explanation"])
# print(result["summary"])

# ✅ Task 2 Code – Problem → Solution Chain

# Chain 1 --> Expand Problem
# problem_prompt = PromptTemplate(
#     input_variables = ["problem"],
#     template="The user has the problem: {problem}. Explain the problem in detailed, why it happen, and its impact"
# )
# problem_chain = LLMChain(llm=llm, prompt=problem_prompt, output_key="detailed_problem")

# # Chain 2 --> Suggest Solution
# solution_prompt = PromptTemplate(
#     input_variables = ["detailed_problem"],
#     template = "Based on the following description, suggest 3 clear practical solutions: \n\n{detailed_problem}"
# )
# solution_chain = LLMChain(llm=llm, prompt=solution_prompt, output_key="solutions")

# # Sequential Chain
# problem_solution = SequentialChain(
#     chains=[problem_chain,solution_chain],
#     input_variables = ["problem"],
#     output_variables = ["detailed_problem","solutions"]
# )

# user_prompt = input("Enter your problem: ")
# result = problem_solution({"problem": user_prompt})
# print(result)


# Chain 1 --> Character + Place Intro
intro_Prompt = PromptTemplate(
    input_variables = ["charactor","place"],
    template = "Create a short introduction for a character named {charactor} who lives in {place}."
) 
intro_chain = LLMChain(llm=llm,prompt=intro_Prompt, output_key ="intro")

# Chain 2 --> Story Builder
story_prompt = PromptTemplate(
    input_variable = ["intro"],
    template="Based on the introduction below, write a short, engaging story:\n\n{intro}"
)
story_chain = LLMChain(llm=llm,prompt=story_prompt, output_key="story")

# Sequential Chain
story_builder_chain = SequentialChain(
    chains = [intro_chain,story_chain],
    input_variables = ["charactor","place"],
    output_variables = ["intro","story"]
)

charactor = input("Enter you charactor: ")
place = input("Enter your place: ")

result = story_builder_chain({"charactor":charactor,"place":place})

print(result)
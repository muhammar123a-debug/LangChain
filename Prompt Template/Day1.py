from langchain.prompts import PromptTemplate

template = """
Translate the following text to Urdu:

{text}
"""

prompt = PromptTemplate(
    input_variables = ["text"],
    template = template
)
final_prompt = prompt.format(text="I love programming.")

print(final_prompt)
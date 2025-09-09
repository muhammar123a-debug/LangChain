from langchain.prompts import PromptTemplate

# Task 1 (Single Input Variable)
template = """
Translate the following text to Urdu:

{text}
"""
prompt = PromptTemplate(
    input_variables=["text"],
    template=template
)
final_prompt = prompt.format(text="I love programming.")
print(final_prompt)


# Task 2 (Multiple Input Variables)
template2 = """
Write a short introduction for a person.

Name: {name}
Profession: {profession}

Output:
"""
prompt2 = PromptTemplate(
    input_variables=["name", "profession"],   
    template=template2                        
)

final_prompt2 = prompt2.format(name="Alice", profession="Data Scientist")
print(final_prompt2)

# Task 3 Default instruction + user input combine

template3 = """
Summarize the following text in one sentence.

text: {text}
"""

prompt3 = PromptTemplate(
    input_variables=["text"],
    template=template3
)

final_prompt3 = prompt.format(text="Artificial Intelligence is transforming industries by automating tasks, improving decision-making, and enhancing user experiences. It is being widely adopted in healthcare, finance, and education to create smarter systems.")
print(final_prompt3)

# Task 4 Multiple Variables with Tone Control
template4 = """
Summarize the following paragraph in 2 sentences only.
write the summary in a {tone} tone.

text: {text}

"""
prompt4 = PromptTemplate(
    input_variables=["text", "tone"],
    template=template4
)

final_prompt4 = prompt4.format(
    text="Machine learning is a subset of artificial intelligence that focuses on building systems that can learn from and make decisions based on data. It involves various algorithms and statistical models to analyze patterns and improve performance over time without being explicitly programmed.",
    tone="professional"
)
print(final_prompt4)

# Task 5 – Role-Based Prompt
template5 ="""
You are an experianced English Teacher.
Your task is to explain the following word in simple terms.
with an example sentence.

Word: {word}
"""
prompt5 = PromptTemplate(
    imput_variables=["word"],
    template=template5
)

final_prompt5 = prompt5.format(word="Artificial Intelligence")
print(final_prompt5)
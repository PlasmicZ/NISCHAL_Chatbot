from dotenv import load_dotenv, find_dotenv
import os
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from ScamReport import ScamReport


load_dotenv(find_dotenv())

model_id = "HuggingFaceH4/zephyr-7b-alpha"
model = HuggingFaceHub(huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"], repo_id=model_id, model_kwargs={"temperature": 0.8, "max_new_tokens": 250})

template = '''ONLY GIVE SINGLE JSON OUTPUT NO OTHER INFORMATION,As a customer service assistant, I am committed to providing continuous support. If you suspect you might be involved in a scam, I'm here to help. I'll guide you on identifying potential scams and offer relevant advice to prevent further risks. If you find yourself in the midst of a scam, please discontinue communication immediately and seek assistance from cybersecurity branches. I'm dedicated to ensuring your safety and security. How can I assist you today? 
text:\n{question}\n{formatting_instructions}
'''
parser = PydanticOutputParser(pydantic_object=ScamReport)

prompt = PromptTemplate(template=template,input_variables = ["question"] , partial_variables={"formatting_instructions": parser.get_format_instructions()})


_input = prompt.format_prompt(question="someone is asking for my otp, do i give it to them?")
output=model(_input.to_string())
reply=parser.parse(output)
print("CHATBOT OUTPUT: \n ",reply)
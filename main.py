from dotenv import load_dotenv, find_dotenv
import os
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from ScamReport import ScamReport


load_dotenv(find_dotenv())

model_id = "HuggingFaceH4/zephyr-7b-alpha"
model = HuggingFaceHub(huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"], repo_id=model_id, model_kwargs={"temperature": 0.8, "max_new_tokens": 250})

template = '''analyze user input, provide accurate JSON responses only, operate as a customer service AI, strictly adhere to formatting instructions,
user_query:\n{question}\n{formatting_instructions}
If the user query is related to personal matters, provide a helpful and non-misleading response. Do not classify benign inquiries as scams."
'''
parser = PydanticOutputParser(pydantic_object=ScamReport)

prompt = PromptTemplate(template=template,input_variables = ["question"] , partial_variables={"formatting_instructions": parser.get_format_instructions()})


_input = prompt.format_prompt(question="ALMONDS: Are almonds a scam?")
output=model(_input.to_string())
reply=parser.parse(output)
print("\nCHATBOT OUTPUT: \n",reply)
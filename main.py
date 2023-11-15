from dotenv import load_dotenv, find_dotenv
import os
from langchain import HuggingFaceHub, PromptTemplate, LLMChain

load_dotenv(find_dotenv())

model_id = "tiiuae/falcon-7b-instruct"
model = HuggingFaceHub(huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"], repo_id=model_id,model_kwargs={"temperature":0.6,"max_new_tokens":100})

template = '''never say you are an ai model,You are a polite customer service assistant ,tell people if they are being scammed or not, must help prevent scam by giving relevant replies to scam victims or potential scam victims,if they are being scammed ask them to cut off contact and request help from cybersecurity branches
{query}
'''

prompt = PromptTemplate(template=template, input_variables=['query'])
conv_chain = LLMChain(llm=model, prompt=prompt, verbose=True)

print(conv_chain.run("Someone is asking for my otp do i give it to them?"))

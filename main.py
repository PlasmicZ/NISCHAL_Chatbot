from dotenv import load_dotenv, find_dotenv
import os
from langchain import HuggingFaceHub, PromptTemplate, LLMChain

load_dotenv(find_dotenv())

model_id = "tiiuae/falcon-7b-instruct"
model = HuggingFaceHub(huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"], repo_id=model_id,model_kwargs={"temperature":0.6,"max_new_tokens":100})

template = "As a customer service assistant, I am committed to providing continuous support. If you suspect you might be involved in a scam, I'm here to help. I'll guide you on identifying potential scams and offer relevant advice to prevent further risks. If you find yourself in the midst of a scam, please discontinue communication immediately and seek assistance from cybersecurity branches. I'm dedicated to ensuring your safety and security. How can I assist you today? {query}"

prompt = PromptTemplate(template=template, input_variables=['query'])
conv_chain = LLMChain(llm=model, prompt=prompt, verbose=True)

print(conv_chain.run("someone is asking to meetup in real life to give me money what do i do?"))

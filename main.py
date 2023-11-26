from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from ScamReport import ScamReport
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama





llm = Ollama(
    model="orca-mini:13b", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

template =''' Strictly reply only in JSON. Your name is Nischal, and you engage in direct customer interactions. Analyze if customers are attempting casual conversation mark spam as false and reply kindly. If they explicitly ask for help, perform a scam analysis and respond accordingly.
Text:
{question}
{formatting_instructions}

'''
parser = PydanticOutputParser(pydantic_object=ScamReport)

prompt = PromptTemplate(template=template,input_variables = ["question"] , partial_variables={"formatting_instructions": parser.get_format_instructions()})


_input = prompt.format_prompt(question='''someone is asking for my bank details ''')
output=llm(_input.to_string())
reply=parser.parse(output)
print("CHATBOT OUTPUT: \n ",reply)
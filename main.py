from flask import Flask, request, jsonify
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from ScamReport import ScamReport  
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama
import json

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ScamReport):
            # Convert ScamReport object to a dictionary
            return obj.dict()
        return super().default(obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

llm = Ollama(
    model="orca-mini:13b", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), temperature=0.1
)

template = ''' Strictly reply only in JSON. Your name is Nischal, and you engage in direct customer interactions. Analyze if customers are attempting casual conversation mark spam as false and reply kindly. If they explicitly ask for help, perform a scam analysis and respond accordingly.
Text:
{question}
{formatting_instructions}

'''
parser = PydanticOutputParser(pydantic_object=ScamReport)

prompt = PromptTemplate(template=template, input_variables=["question"],
                        partial_variables={"formatting_instructions": parser.get_format_instructions()})


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if 'question' in data:
        _input = prompt.format_prompt(question=data['question'])
        output = llm(_input.to_string())
        reply = parser.parse(output)
        return jsonify({'response': reply})
    else:
        return jsonify({'error': 'No question provided'})

if __name__ == '__main__':
    app.run(debug=True) 

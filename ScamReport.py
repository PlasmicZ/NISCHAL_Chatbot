from pydantic import BaseModel, Field

class ScamReport(BaseModel):
    response : str = Field (description="reply like a chatbot")
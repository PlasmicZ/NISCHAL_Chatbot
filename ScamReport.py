from pydantic import BaseModel, Field

class ScamReport(BaseModel):
    is_scam : bool = Field (description="Is the person being scammed or is the person just talking to you? ")
    response : str = Field (description="reply like a chatbot")
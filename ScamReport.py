from pydantic import BaseModel, Field

class ScamReport(BaseModel):
    is_scam : bool = Field (description="Is the person being scammed? ")
    support_request : str = Field(description="What kind of scam is the person facing?")
    in_danger: bool = Field(description="Is the person in danger?")
    response: str = Field(description="steps the person should take to ensure their safety")
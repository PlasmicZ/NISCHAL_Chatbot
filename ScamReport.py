from pydantic import BaseModel, Field

class ScamReport(BaseModel):
    is_scam : bool = Field (description="Is the person being scammed? ")
    in_danger: bool = Field(description="Is the person in danger?")
    been_scammed: bool = Field(description="has the scam happened already?")
    response : str = Field(description="What should the person do?")
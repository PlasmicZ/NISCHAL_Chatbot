from pydantic import BaseModel, Field

class ScamReport(BaseModel):
    is_scam : bool = Field (description="Is the person being scammed? ")
    support_request : str = Field(description="What kind of scam is the person facing?")
    in_danger: bool = Field(description="Is the person in danger?")
    been_scammed: bool = Field(description="has the scam happened already?")
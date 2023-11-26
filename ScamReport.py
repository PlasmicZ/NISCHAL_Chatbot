from pydantic import BaseModel, Field

class ScamReport(BaseModel):
    is_scam : bool = Field (description="Is the person being scammed? ")
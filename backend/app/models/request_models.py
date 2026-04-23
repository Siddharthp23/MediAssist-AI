from pydantic import BaseModel

class HealthcareRequest(BaseModel):
    input_text: str
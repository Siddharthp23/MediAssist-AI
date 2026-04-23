from fastapi import APIRouter
from app.models.request_models import HealthcareRequest
from app.services.agent_service import generate_plan

router = APIRouter()

@router.post("/generate-plan")
def plan(req: HealthcareRequest):
    result = generate_plan(req.input_text)
    return result
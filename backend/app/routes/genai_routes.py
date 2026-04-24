from fastapi import APIRouter
from app.models.request_models import HealthcareRequest
from app.services.genai_service import generate_summary

router = APIRouter()

@router.post("/generate-summary")
def summary(req: HealthcareRequest):
    result = generate_summary(req.input_text)
    return {"summary": result}

@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "MediAssist AI backend is running"
    }

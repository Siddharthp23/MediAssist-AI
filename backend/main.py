from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import genai_routes, agent_routes

app = FastAPI()

# ✅ ADD THIS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(genai_routes.router)
app.include_router(agent_routes.router)
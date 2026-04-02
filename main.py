

from __future__ import annotations

from fastapi import FastAPI

from models import CEORequest, CEOResponse
from orchestrator import run_orchestrator


app = FastAPI(title="AI CEO")


@app.get("/")
async def root():
    return {"status": "AI CEO running"}


@app.post("/ceo/run", response_model=CEOResponse)
async def run_ceo(request: CEORequest):
    return await run_orchestrator(request)


from __future__ import annotations

from typing import List
from pydantic import BaseModel


class CEORequest(BaseModel):
    goal: str


class CEOAction(BaseModel):
    action: str


class CEOResponse(BaseModel):
    plan: str
    actions: List[str]
    reasoning: str
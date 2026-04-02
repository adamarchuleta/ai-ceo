from __future__ import annotations

import os
import httpx

from models import CEORequest, CEOResponse
from config import settings


async def run_ceo_agent(request: CEORequest) -> CEOResponse:
    if not settings.OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is not set")

    system_prompt = (
        "You are an AI CEO. Your job is to think like a startup founder. "
        "Given a goal, create a clear plan, a short list of concrete actions, "
        "and explain your reasoning."
    )

    user_prompt = (
        f"Goal: {request.goal}\n\n"
        "Return a JSON response with keys: plan, actions, reasoning."
    )

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": settings.OPENAI_MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "temperature": 0.3,
            },
        )
        response.raise_for_status()
        data = response.json()

    content = data["choices"][0]["message"]["content"]

    # naive parsing (we’ll improve later)
    try:
        import json

        parsed = json.loads(content)
        return CEOResponse(
            plan=parsed.get("plan", ""),
            actions=parsed.get("actions", []),
            reasoning=parsed.get("reasoning", ""),
        )
    except Exception:
        # fallback if model doesn't return valid JSON
        return CEOResponse(
            plan=content,
            actions=[],
            reasoning="",
        )
from __future__ import annotations

from models import CEORequest, CEOResponse
from agent import run_ceo_agent
from memory import add_memory


async def run_orchestrator(request: CEORequest) -> CEOResponse:
    """
    Orchestrator layer.

    For v1, this simply calls the agent once.
    This file exists to separate decision flow from the raw LLM call,
    making it easy to extend into multi-step reasoning later.
    """

    # Step 1: initial reasoning
    response = await run_ceo_agent(request)

    # Store decision in memory
    add_memory({
        "goal": request.goal,
        "plan": response.plan,
        "actions": response.actions,
        "reasoning": response.reasoning,
    })

    # Future:
    # - iterate on actions
    # - call tools
    # - store memory

    return response
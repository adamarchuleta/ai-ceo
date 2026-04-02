

from __future__ import annotations

from typing import List, Dict


# Simple in-memory store (v1)
# Later this can be replaced with SQLite, Redis, or a vector DB
_MEMORY: List[Dict] = []


def add_memory(entry: Dict) -> None:
    """Store a decision/action in memory."""
    _MEMORY.append(entry)


def get_memory() -> List[Dict]:
    """Return all stored memory."""
    return _MEMORY


def clear_memory() -> None:
    """Clear all memory (useful for testing)."""
    _MEMORY.clear()
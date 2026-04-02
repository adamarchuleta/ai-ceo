


# AI CEO

A minimal agent that plans, decides, and executes like a startup founder.

This project demonstrates how to build an LLM-powered decision engine that takes a goal and produces a structured plan, concrete actions, and reasoning.

---

## Quick Start

```
pip install -r requirements.txt
python3 -m uvicorn main:app --reload --port 8003
```

Open:

```
http://127.0.0.1:8003/docs
```

---

## Overview

AI CEO is a simple agent that simulates how a founder would think about a problem.

Given a goal, it:

1. Creates a high-level plan
2. Breaks it into actionable steps
3. Explains the reasoning behind the decisions

---

## Example

### Request

```
{
  "goal": "Grow a SaaS app to 100 users"
}
```

### Response

```
{
  "plan": "Focus on distribution and rapid iteration",
  "actions": [
    "Post daily short-form content",
    "Reach out to early users",
    "Ship weekly improvements"
  ],
  "reasoning": "Early-stage growth depends on visibility and fast feedback loops"
}
```

---

## Architecture

```
Goal Input
   ↓
LLM Reasoning (Agent)
   ↓
Structured Output (Plan + Actions + Reasoning)
```

---

## Project Structure

```
main.py         → API
agent.py        → LLM reasoning
models.py       → request/response schemas
```

---

## Requirements

- Python 3.9+
- OpenAI API key

---

## Setup

### 1. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Create `.env`

```
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4.1-mini
```

---

## Run

```
python3 -m uvicorn main:app --reload --port 8003
```

---

## Notes

- This is a minimal agent implementation
- No memory or tool execution (yet)
- Designed to be extended into a full agent system

---

## Future Improvements

- Memory (stateful decision making)
- Tool execution (API actions)
- Multi-step reasoning loop
- Integration with other services

---

## License

MIT
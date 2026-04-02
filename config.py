

from __future__ import annotations

import os
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv(override=True)


class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


settings = Settings()
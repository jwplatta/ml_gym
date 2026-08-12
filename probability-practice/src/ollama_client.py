#!/usr/bin/env python3
"""
Ollama client for prompt-only generation.
"""

from __future__ import annotations

import os

import ollama
from dotenv import load_dotenv

DEFAULT_HOST = "http://localhost:11434"
DEFAULT_MODEL = "gpt-oss:120b-cloud"
DEBUG_ENV_VAR = "OLLAMA_DEBUG"


def request_ollama(
    prompt: str,
    *,
    model: str | None = None,
    host: str | None = None,
    timeout: int = 60,
) -> str:
    load_dotenv()
    api_key = os.getenv("OLLAMA_API_KEY")
    debug_enabled = os.getenv(DEBUG_ENV_VAR, "").lower() in {"1", "true", "yes"}

    model_name = model or DEFAULT_MODEL
    host_name = host or os.getenv("OLLAMA_HOST") or DEFAULT_HOST

    headers = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    client = ollama.Client(
        host=host_name,
        headers=headers or None,
        timeout=timeout,
    )

    response = client.generate(
        model=model_name,
        prompt=prompt,
        stream=False,
    )

    output_text = response.get("response", "")
    if output_text:
        return output_text

    if debug_enabled:
        raise RuntimeError(f"No response text found. Raw response: {response}")

    raise RuntimeError("No response text found. Set OLLAMA_DEBUG=1 to print raw response.")

#!/usr/bin/env python3
"""
OpenRouter client for responses and chat/completions endpoints.
"""

from __future__ import annotations

import os
import time
from typing import Literal

import requests
from dotenv import load_dotenv

# DEFAULT_MODEL = "openai/gpt-oss-120b:free"
# DEFAULT_MODEL = "meta-llama/llama-3.3-70b-instruct:free"
DEFAULT_MODEL = "qwen/qwen3-next-80b-a3b-instruct:free"

RESPONSES_URL = "https://openrouter.ai/api/v1/responses"
CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
DEBUG_ENV_VAR = "OPENROUTER_DEBUG"

Endpoint = Literal["responses", "chat"]


def resolve_endpoint(model: str, endpoint: Endpoint | None) -> Endpoint:
    if endpoint:
        return endpoint

    if model.startswith("qwen/"):
        return "chat"

    return "responses"


def extract_output_text(payload: dict) -> str:
    if not isinstance(payload, dict):
        return ""

    if payload.get("output_text"):
        return payload["output_text"]

    output_items = payload.get("output")
    if isinstance(output_items, list):
        chunks = []
        for item in output_items:
            if not isinstance(item, dict):
                continue
            content = item.get("content")
            if not isinstance(content, list):
                continue
            for part in content:
                if not isinstance(part, dict):
                    continue
                if part.get("type") == "output_text" and part.get("text"):
                    chunks.append(part["text"])
        return "\n".join(chunks)

    choices = payload.get("choices")
    if isinstance(choices, list) and choices:
        message = choices[0].get("message", {})
        if isinstance(message, dict):
            content = message.get("content")
            if isinstance(content, str):
                return content

    return ""


def request_openrouter(
    prompt: str,
    *,
    model: str,
    timeout: int = 60,
    endpoint: Endpoint | None = None,
    max_retries: int = 3,
) -> str:
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    debug_enabled = os.getenv(DEBUG_ENV_VAR, "").lower() in {"1", "true", "yes"}

    if not api_key:
        raise RuntimeError("Missing OPENROUTER_API_KEY env var")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    endpoint = resolve_endpoint(model, endpoint)
    if endpoint == "chat":
        url = CHAT_URL
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        }
    else:
        url = RESPONSES_URL
        payload = {
            "model": model,
            "input": prompt,
        }

    response = None
    for attempt in range(1, max_retries + 1):
        response = requests.post(url, headers=headers, json=payload, timeout=timeout)
        if response.status_code not in {429, 500, 502, 503, 504}:
            break

        if attempt == max_retries:
            response.raise_for_status()

        retry_after = response.headers.get("Retry-After")
        sleep_seconds = None

        if retry_after:
            try:
                sleep_seconds = float(retry_after)
            except ValueError:
                sleep_seconds = None

        if sleep_seconds is None:
            sleep_seconds = 2.0 * attempt

        time.sleep(sleep_seconds)

    response.raise_for_status()
    data = response.json()

    output_text = extract_output_text(data)
    if output_text:
        return output_text

    if debug_enabled:
        raise RuntimeError(f"No output_text found. Raw response: {data}")

    raise RuntimeError("No output_text found. Set OPENROUTER_DEBUG=1 to print raw response.")

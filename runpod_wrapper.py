import runpod
from typing import Any, Literal, TypedDict
import requests
import sys

class HandlerInput(TypedDict):
    method_name: Literal["generate"]
    input: Any


class HandlerJob(TypedDict):
    input: HandlerInput


def handler(job: HandlerJob):
    ollama_url = "http://0.0.0.0:11434"
    model = sys.argv[1]
    system = job["system"]

    input = {
        "stream": False,
        "model": model,
        "prompt": job["prompt"],
    }

    if system:
        input["system"] = system

    response = requests.post(
        url=f"{ollama_url}/api/generate/",
        headers={"Content-Type": "application/json"},
        json=input,
    )
    response.encoding = "utf-8"

    return response.json()


runpod.serverless.start({"handler": handler})

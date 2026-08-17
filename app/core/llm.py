from typing import Protocol


class LLMClient(Protocol):
    async def generate(self, message: str) -> str: ...


class FakeLLMClient:
    async def generate(self, message: str) -> str:
        return f"Fake AI: {message}"

from app.core.llm import LLMClient


class ChatService:
    def __init__(self, llm: LLMClient) -> None:
        self.llm = llm

    async def chat(self, message: str) -> str:
        return await self.llm.generate(message)

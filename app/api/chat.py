from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()


from app.core.llm import FakeLLMClient

chat_service = ChatService(
    llm=FakeLLMClient(),
)


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    message = await chat_service.chat(request.message)

    return ChatResponse(message=message)

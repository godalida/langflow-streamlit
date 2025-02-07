from typing import Optional
from pydantic import BaseModel
from langflow_streamlit.utils import settings


class ChatModel(BaseModel):
    title: str = "Welcome to The Table Search Tool!
    welcome_msg: str = "Feel free to ask questions regarding the Message of the Hour"
    write_speed: float = 0.05
    input_msg: str = "Ask some question..."
    ai_avatar: Optional[str] = None
    user_avatar: Optional[str] = None
    port: int = settings.STREAMLIT_PORT
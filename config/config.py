from pydantic_settings import BaseSettings
from typing import Optional
class Settings(BaseSettings):
    pine_api:Optional[str] = None
    google_api: Optional[str] = None

    pinecone_env: str = "us-east-1"
    pinecone_idx: str = "llama-text-embed-v2-index"
    embed_model: str = "llama-text-embed-v2"

    chat_model: str = "gemini-2.5-flash"

    ollama_port:str = "11434"
    fallback_chat_model:str = "gemma3:4b"
    fallback_embed_model: str = "embeddinggemma:300m"

    class Config:
        env = ".env"


settings = Settings()

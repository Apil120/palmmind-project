from datetime import datetime
from pydantic import BaseModel, Field
from typing import List,Optional
from enum import Enum

class ChunkingStrategy(str, Enum):
    FIXED_SIZE = "fixed_size"
    SEMANTIC = "semantic"


class DocumentUpload(BaseModel):
    chunking_strategy: ChunkingStrategy = ChunkingStrategy.FIXED_SIZE
    chunk_size: int = Field(default=512, ge=100, le=2048)
    chunk_overlap: int = Field(default=50, ge=0, le=200)


class DocumentResponse(BaseModel):
    document_id: str
    filename: str
    chunks_count: int
    status: str


class ChatMessage(BaseModel):
    message: str
    session_id: str


class ChatResponse(BaseModel):
    response: str
    session_id: str
    sources: List[str] = []


class InterviewBooking(BaseModel):
    name: str
    email: str
    date: str
    time: str


class BookingStatus(str,Enum):
    booked = "booked"
    calcelled = "cancelled"
    completed =  "completed"
    postponsed = "postponed"
    preponed = "preponed"
class BookingResponse(BaseModel):
    booking_id: str
    status: BookingStatus
    details: InterviewBooking


class DocumentMetaData(BaseModel):
    id: str
    filename: str
    upload_date: datetime
    chunking_strategy: str
    chunks_count: int
    total_size: Optional[int] = None
    metadata: Optional[dict[str,str]] = {}

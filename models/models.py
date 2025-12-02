from pydantic import BaseModel
from enum import Enum

class ChunkingStrategy(str, Enum):
    FIXED_SIZE = "fixed_size"
    SEMANTIC = "semantic"
    RECURSIVE="recursive"


class RequestBody(BaseModel):
    chunking_strat:ChunkingStrategy
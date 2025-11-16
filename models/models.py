from pydantic import BaseModel


class History(BaseModel):
    n_exchanges = int
    history = list[dict[str,str]]
class Request(BaseModel):
    chat_history:History
    message:str

class Response(BaseModel):
    interview_details: list[dict[str,str]]
    reply:str
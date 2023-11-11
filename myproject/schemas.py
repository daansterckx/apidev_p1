from pydantic import BaseModel




class ClientBase(BaseModel):
    name: str

class ClientCreate(ClientBase):
    password: str


class Client(ClientBase):
    id: int
    class Config:
        orm_mode = True
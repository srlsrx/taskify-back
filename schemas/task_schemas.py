

from pydantic import BaseModel
from schemas.user_schemas import UserOut

class TaskBase(BaseModel):
    name: str
    description: str | None = None
    is_done: bool = False

class TaskCreate(TaskBase):
    user_id: int

class TaskOut(TaskBase):
    id: int
    user: UserOut | None = None

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    is_done: bool | None = None
    user_id: int | None = None

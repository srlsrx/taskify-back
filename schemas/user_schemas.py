from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    is_admin: bool

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    password: str

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None
    is_admin: bool | None = None

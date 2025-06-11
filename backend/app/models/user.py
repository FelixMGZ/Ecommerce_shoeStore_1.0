from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Annotated

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    rol: str = "USER"

class UserCreate(UserBase):
    password: Annotated[str, Field(min_length=6)]

class UserOut(UserBase):
    id: str

class UserInDB(UserBase):
    id: str
    hashed_password: str
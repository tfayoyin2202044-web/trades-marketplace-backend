from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str
    trade: Optional[str] = None
    location: Optional[str] = None


class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str
    trade: Optional[str]
    location: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class JobCreate(BaseModel):
    title: str
    description: str
    trade_needed: str
    location: str


class JobOut(BaseModel):
    id: int
    title: str
    description: str
    trade_needed: str
    location: str
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
  access_token: str
  token_type: str
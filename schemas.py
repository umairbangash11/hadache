from typing import Optional
from pydantic import BaseModel

class SignInRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserIn(BaseModel):
    username: str
    password: str
    email: str

class UserRead(BaseModel):
    username: str
    email: str
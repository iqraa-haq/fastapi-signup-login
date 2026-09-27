from pydantic import BaseModel, EmailStr
#Library jo data ko automatically validate karti hai (sahi format mein hai ya nahi check karti hai).

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
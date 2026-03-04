from pydantic import BaseModel, EmailStr
from uuid import UUID

class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
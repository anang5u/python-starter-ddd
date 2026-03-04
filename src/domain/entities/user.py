from dataclasses import dataclass
from uuid import UUID, uuid4

@dataclass
class User:
    id: UUID
    name: str
    email: str

    @staticmethod
    def create(name: str, email: str):
        if "@" not in email:
            raise ValueError("Invalid email")
        return User(id=uuid4(), name=name, email=email)
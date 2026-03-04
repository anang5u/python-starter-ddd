from uuid import UUID
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository

class UserUseCase:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create(self, name: str, email: str) -> User:
        user = User.create(name, email)
        self.repo.save(user)
        return user
    
    def get_by_id(self, user_id: UUID):
        return self.repo.get_by_id(user_id)
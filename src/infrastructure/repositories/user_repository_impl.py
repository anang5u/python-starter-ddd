from uuid import UUID
from sqlalchemy import Column, String
from sqlalchemy.orm import Session
from infrastructure.database import Base
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository

class UserModel(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)


class SQLAlchemyUserRepository(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    def save(self, user: User) -> None:
        model = UserModel(
            id=str(user.id),
            name=user.name,
            email=user.email
        )
        self.db.add(model)
        self.db.commit()

    def get_by_id(self, user_id: UUID) -> User | None:
        model = self.db.query(UserModel).filter_by(id=str(user_id)).first()
        if not model:
            return None
        return User(id=UUID(model.id), name=model.name, email=model.email)
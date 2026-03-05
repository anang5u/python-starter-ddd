from uuid import UUID
from sqlalchemy.orm import Session
from infrastructure.database.models.user_model import Base, UserModel
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository

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
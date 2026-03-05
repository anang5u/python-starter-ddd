from sqlalchemy import Column, String
from infrastructure.database.base import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
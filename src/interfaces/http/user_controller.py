from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from infrastructure.repositories.user_repository_impl import SQLAlchemyUserRepository
from application.usecases.user_uc import UserUseCase
from interfaces.http.schemas import CreateUserRequest
from infrastructure.database import get_db

router = APIRouter()

@router.post("/users", status_code=201)
def create_user(req: CreateUserRequest, db: Session = Depends(get_db)):
    repo = SQLAlchemyUserRepository(db)
    usecase = UserUseCase(repo)
    user = usecase.create(req.name, req.email)
    return user

@router.get("/users/{user_id}")
def get_user(user_id: str, db: Session = Depends(get_db)):
    repo = SQLAlchemyUserRepository(db)
    usecase = UserUseCase(repo)
    return usecase.get_by_id(user_id)
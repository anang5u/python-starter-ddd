from uuid import UUID
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from infrastructure.database.database import Base
from domain.entities.indicator import Indicator
from domain.repositories.indicator_repository import IndicatorRepository


class SQLAlchemyIndicatorRepository(IndicatorRepository):

    def __init__(self, db: Session):
        self.db = db

    def get(self) -> list[Indicator]:
        models = self.db.query(IndicatorModel).filter_by(active=1).all()
        
        return [
            Indicator(
                id=UUID(m.id), 
                code=m.code, 
                name=m.name, 
                description=m.description
            ) for m in models
        ]
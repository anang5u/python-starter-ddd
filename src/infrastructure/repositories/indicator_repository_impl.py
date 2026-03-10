from uuid import UUID
from sqlalchemy.orm import Session
from infrastructure.database.models.indicator_model import IndicatorModel
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
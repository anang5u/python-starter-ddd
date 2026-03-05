from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func

from infrastructure.database.base import Base


class IndicatorModel(Base):
    __tablename__ = "indicator"

    id = Column(String, primary_key=True)
    code = Column(String, unique=True, index=True)
    name = Column(String)
    description = Column(String)
    active = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
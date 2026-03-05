import uuid
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.engine import Engine

from infrastructure.database.base import Base
from infrastructure.database.models.indicator_model import IndicatorModel


INITIAL_INDICATORS = [
    {
        "code": "IND_POVERTY",
        "name": "Indikator Kemiskinan",
        "description": "Data penduduk miskin",
        "active": 1,
    }
]


def seed_data(db: Session, model_class, data_list: list, unique_key: str):

    for item in data_list:

        exists = db.query(model_class).filter(
            getattr(model_class, unique_key) == item[unique_key]
        ).first()

        if exists:
            continue

        data = dict(item)

        if "id" not in data:
            data["id"] = str(uuid.uuid4())

        obj = model_class(**data)

        db.add(obj)


def run_automigrate(engine: Engine):

    print("Starting automigrate...")

    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()

    try:

        seed_data(
            db,
            IndicatorModel,
            INITIAL_INDICATORS,
            unique_key="code",
        )

        db.commit()

        print("Automigrate success")

    except Exception as e:

        db.rollback()

        print(f"Automigrate error: {e}")

        raise

    finally:
        db.close()
from infrastructure.database.database import init_engine
from infrastructure.database.database import get_session_factory


def test_engine_creation(monkeypatch):
    monkeypatch.setenv("APP_ENV", "development")
    monkeypatch.setenv("DB_URL", "sqlite:///:memory:")

    engine = init_engine()

    assert engine is not None
    assert "sqlite" in str(engine.url)

def test_session_factory(monkeypatch):
    monkeypatch.setenv("DB_URL", "sqlite:///:memory:")

    SessionLocal = get_session_factory()
    session = SessionLocal()

    assert session is not None
    session.close()
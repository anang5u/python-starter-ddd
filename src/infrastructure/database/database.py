import logging
import time

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from sqlalchemy.pool import StaticPool

from infrastructure.config import settings
from infrastructure.database.automigrate import run_automigrate

logger = logging.getLogger(__name__)

_engine: Engine | None = None
_SessionLocal: sessionmaker | None = None


def init_engine() -> Engine:
    """
    Initialize SQLAlchemy engine using environment-based config.
    Idempotent: hanya dibuat sekali.
    """
    global _engine

    if _engine is None:
        _engine = create_engine(
            settings.database.url,
            pool_size=settings.database.pool_size,
            max_overflow=settings.database.max_overflow,
            pool_pre_ping=True,  # penting untuk production
            echo=settings.environment == "development",  # auto debug SQL
            future=True,
        )

    return _engine


def get_session_factory() -> sessionmaker:
    """
    Return sessionmaker (lazy init).
    """
    global _SessionLocal

    if _SessionLocal is None:
        engine = init_engine()
        _SessionLocal = sessionmaker(
            bind=engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    return _SessionLocal

def setup_sql_debug(engine):

    @event.listens_for(engine, "before_cursor_execute")
    def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        conn.info.setdefault("query_start_time", []).append(time.time())

        logger.debug(f"SQL: {statement}")
        logger.debug(f"PARAMS: {parameters}")

    @event.listens_for(engine, "after_cursor_execute")
    def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        total = time.time() - conn.info["query_start_time"].pop()

        logger.debug(f"SQL TIME: {total:.4f}s")

def get_db():
    """
    FastAPI dependency.
    """
    SessionLocal = get_session_factory()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db_test():

    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    setup_sql_debug(engine)
    run_automigrate(engine)
    SessionLocal = sessionmaker(bind=engine)

    return SessionLocal()
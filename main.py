from fastapi import FastAPI
from contextlib import asynccontextmanager

from interfaces.http.user_controller import router
from infrastructure.database import init_engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    engine = init_engine()
    Base.metadata.create_all(bind=engine)

    yield

    # SHUTDOWN (optional)
    # misalnya close engine kalau perlu


app = FastAPI(lifespan=lifespan)

app.include_router(router)
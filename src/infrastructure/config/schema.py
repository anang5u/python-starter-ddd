from pydantic import BaseModel

class AppConfig(BaseModel):
    name: str
    version: str


class DatabaseConfig(BaseModel):
    url: str
    pool_size: int
    max_overflow: int


class ObservabilityConfig(BaseModel):
    slow_query_threshold: float
    enable_metrics: bool


class Settings(BaseModel):
    app: AppConfig
    database: DatabaseConfig
    observability: ObservabilityConfig
    environment: str
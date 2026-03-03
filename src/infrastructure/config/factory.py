import os
from pydantic import ValidationError
from infrastructure.config.schema import Settings
from infrastructure.config.loader import load_yaml, deep_merge


def build_config() -> Settings:
    env = os.getenv("APP_ENV", "development")

    base_config = load_yaml("config/base.yaml")
    env_config = load_yaml(f"config/{env}.yaml")

    merged = deep_merge(base_config, env_config)

    # ENV override priority
    db_url = os.getenv("DB_URL")
    if db_url:
        merged.setdefault("database", {})["url"] = db_url

    merged["environment"] = env

    try:
        return Settings(**merged)
    except ValidationError as e:
        raise RuntimeError(f"Invalid configuration: {e}")
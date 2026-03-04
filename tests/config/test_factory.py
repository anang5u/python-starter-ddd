from infrastructure.config.factory import build_config
import pytest
from infrastructure.config.schema import Settings


def test_build_config_development(monkeypatch):
    monkeypatch.setenv("APP_ENV", "development")

    config = build_config()

    assert config.environment == "development"
    assert config.database.url.startswith("sqlite")

def test_env_override(monkeypatch):
    monkeypatch.setenv("APP_ENV", "development")
    monkeypatch.setenv("DB_URL", "sqlite:///override.db")

    config = build_config()

    assert config.database.url == "sqlite:///override.db"

def test_invalid_config():
    with pytest.raises(Exception):
        Settings(app={}, database={}, observability={}, environment="dev")
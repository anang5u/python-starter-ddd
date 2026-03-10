from infrastructure.config.onthology.factory import load_dimension_patterns

def test_load_dimension_patterns(monkeypatch):
    monkeypatch.setenv("APP_ENV", "development")

    patterns = load_dimension_patterns()

    print(patterns)

    #assert config.environment == "development"
    #assert config.database.url.startswith("sqlite")
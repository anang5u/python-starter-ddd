from infrastructure.config.loader import deep_merge

def test_deep_merge_override():
    base = {"a": 1, "b": {"c": 2}}
    override = {"b": {"c": 3}}

    result = deep_merge(base, override)

    assert result["b"]["c"] == 3
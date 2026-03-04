import pytest
from domain.entities.user import User

def test_create_user_success():
    user = User.create("Anang", "anang@mail.com")
    assert user.email == "anang@mail.com"

def test_invalid_email():
    with pytest.raises(ValueError):
        User.create("Anang", "invalid")
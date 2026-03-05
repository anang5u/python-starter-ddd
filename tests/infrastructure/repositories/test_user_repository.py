from infrastructure.database.database import get_db_test
from infrastructure.repositories.user_repository_impl import SQLAlchemyUserRepository
from domain.entities.user import User

def test_save_and_get_user():
    db = get_db_test()

    repo = SQLAlchemyUserRepository(db)
    user = User.create("Anang", "anang@mail.com")

    repo.save(user)
    found = repo.get_by_id(user.id)

    assert found.email == "anang@mail.com"
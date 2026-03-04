from application.usecases.user_uc import UserUseCase
from domain.entities.user import User

class FakeRepo:
    def __init__(self):
        self.saved = None

    def save(self, user: User):
        self.saved = user

    def get_by_id(self, user_id):
        return None

def test_create_user_usecase():
    repo = FakeRepo()
    usecase = UserUseCase(repo)

    user = usecase.create("Anang", "anang@mail.com")

    assert repo.saved == user
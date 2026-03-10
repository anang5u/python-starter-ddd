from infrastructure.database.database import get_db_test
from infrastructure.repositories.indicator_repository_impl import SQLAlchemyIndicatorRepository
from domain.entities.indicator import Indicator

def test_get():
    db = get_db_test()

    repo = SQLAlchemyIndicatorRepository(db)

    results = repo.get()

    print("disini....")
    print(results)
    
    # Assert
    assert len(results) == 1
    assert isinstance(results[0], Indicator)
    assert str(results[0].code) == "IND_POVERTY"
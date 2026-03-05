from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Indicator:
    id: UUID
    code: str
    name: str
    description: str

    @staticmethod
    def create(code: str, name: str, description: str = ""):
        if not code:
            raise ValueError("Indicator code is required")

        if not name:
            raise ValueError("Indicator name is required")

        return Indicator(
            id=uuid4(),
            code=code,
            name=name,
            description=description,
        )
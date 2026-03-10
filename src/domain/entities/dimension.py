from dataclasses import dataclass
from uuid import UUID


@dataclass
class Dimension:
    id: UUID
    code: str
    name: str
    description: str | None = None

    def __repr__(self):
        return f"Dimension(id=UUID('{self.id}'), code='{self.code}', name='{self.name}', description='{self.description}')"

# Contoh Instannce
# Dimension(
#     id=UUID("..."),
#     code="gender",
#     name="Jenis Kelamin",
#     description="Dimensi berdasarkan jenis kelamin"
# )
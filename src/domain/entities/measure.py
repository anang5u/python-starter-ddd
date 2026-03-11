from dataclasses import dataclass
from uuid import UUID


@dataclass
class Measure:
    id: UUID
    code: str
    name: str
    unit: str
    description: str

    def __repr__(self):
        return f"Measure(id=UUID('{self.id}'), code='{self.code}', name='{self.name}', unit='{self.unit}', description='{self.description}')"

# Contoh Instannce
# Dimension(
#     id=UUID("..."),
#     code="gender",
#     name="Jenis Kelamin",
#     description="Dimensi berdasarkan jenis kelamin"
# )
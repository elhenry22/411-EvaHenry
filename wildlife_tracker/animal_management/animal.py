from typing import Any, Optional

class Animal:
    def __init__(self, animal_id: int, species: str, health_status: Optional[str] = None):
        self.animal_id: int = animal_id
        self.species: str = species
        self.health_status: Optional[str] = health_status


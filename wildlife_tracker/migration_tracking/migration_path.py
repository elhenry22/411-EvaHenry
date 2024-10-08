from typing import Optional

class MigrationPath:
    def __init__(self, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None):
        self.species: str = species
        self.start_location: Habitat = start_location
        self.destination: Habitat = destination
        self.duration: Optional[int] = duration

def get_migration_path_by_id(path_id: int) -> MigrationPath:
    pass

def get_migration_paths() -> list[MigrationPath]:
    pass

def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:
    pass

def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
    pass

def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
    pass

def get_migration_path_details(path_id) -> dict:
    pass

def remove_migration_path(path_id: int) -> None:
    pass
    
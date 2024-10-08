from typing import Any
from wildlife_tracker.migration_management.migration_path import MigrationPath

class Migration:
    def __init__(self, migration_id: int, migration_path: MigrationPath):
        self.migration_id: int = migration_id
        self.migration_path: MigrationPath = migration_path
        self.status: str = "Scheduled"

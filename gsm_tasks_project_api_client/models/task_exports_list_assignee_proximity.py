from enum import Enum


class TaskExportsListAssigneeProximity(str, Enum):
    AWAY = "away"
    NEAR = "near"

    def __str__(self) -> str:
        return str(self.value)

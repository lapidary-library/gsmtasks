from enum import Enum


class TasksListAssigneeProximity(str, Enum):
    AWAY = "away"
    NEAR = "near"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class AssigneeProximityEnum(str, Enum):
    AWAY = "away"
    NEAR = "near"

    def __str__(self) -> str:
        return str(self.value)

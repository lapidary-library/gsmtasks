from enum import Enum


class TaskExpiryStateEnum(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"

    def __str__(self) -> str:
        return str(self.value)

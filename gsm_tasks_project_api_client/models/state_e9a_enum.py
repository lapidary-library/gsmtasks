from enum import Enum


class StateE9AEnum(str, Enum):
    PENDING = "pending"
    STARTED = "started"
    COMPLETED = "completed"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)

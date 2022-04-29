from enum import Enum


class TaskCommandStateEnum(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)

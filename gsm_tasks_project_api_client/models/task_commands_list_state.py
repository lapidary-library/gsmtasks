from enum import Enum


class TaskCommandsListState(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)

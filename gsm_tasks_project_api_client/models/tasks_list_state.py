from enum import Enum


class TasksListState(str, Enum):
    UNASSIGNED = "unassigned"
    ASSIGNED = "assigned"
    ACCEPTED = "accepted"
    TRANSIT = "transit"
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

    def __str__(self) -> str:
        return str(self.value)

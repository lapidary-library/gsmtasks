from enum import Enum


class FromStateEnum(str, Enum):
    UNASSIGNED = "unassigned"
    ASSIGNED = "assigned"
    ACCEPTED = "accepted"
    TRANSIT = "transit"
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    AWAY = "away"
    NEAR = "near"

    def __str__(self) -> str:
        return str(self.value)

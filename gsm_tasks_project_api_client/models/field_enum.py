from enum import Enum


class FieldEnum(str, Enum):
    STATE = "state"
    ASSIGNEE_PROXIMITY = "assignee_proximity"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class TaskEventsListField(str, Enum):
    VALUE_0 = ""
    STATE = "state"
    ASSIGNEE_PROXIMITY = "assignee_proximity"

    def __str__(self) -> str:
        return str(self.value)

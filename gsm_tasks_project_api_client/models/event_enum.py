from enum import Enum


class EventEnum(str, Enum):
    CREATE = "create"
    ASSIGN = "assign"
    UNASSIGN = "unassign"
    REJECT = "reject"
    ACCEPT = "accept"
    UNACCEPT = "unaccept"
    TRANSIT = "transit"
    ACTIVATE = "activate"
    COMPLETE = "complete"
    FAIL = "fail"
    CANCEL = "cancel"
    ASSIGNEE_NEAR = "assignee_near"
    ASSIGNEE_AWAY = "assignee_away"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class TaskCommandsListAction(str, Enum):
    UPDATE = "update"
    REASSIGN = "reassign"
    ASSIGN = "assign"
    ACCEPT = "accept"
    UNACCEPT = "unaccept"
    REJECT = "reject"
    UNASSIGN = "unassign"
    TRANSIT = "transit"
    ACTIVATE = "activate"
    COMPLETE = "complete"
    FAIL = "fail"
    CANCEL = "cancel"
    ASSIGNEE_NEAR = "assignee_near"
    ASSIGNEE_AWAY = "assignee_away"

    def __str__(self) -> str:
        return str(self.value)

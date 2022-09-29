from __future__ import annotations

import typing
import lapidary_base
import pydantic
import enum


class ActionEnum(enum.Enum):
    update = "update"
    reassign = "reassign"
    assign = "assign"
    accept = "accept"
    unaccept = "unaccept"
    reject = "reject"
    unassign = "unassign"
    transit = "transit"
    activate = "activate"
    complete = "complete"
    fail = "fail"
    cancel = "cancel"
    assignee_near = "assignee_near"
    assignee_away = "assignee_away"

from __future__ import annotations

import typing
import lapidary_base
import pydantic
import enum
class EventEnum(enum.Enum):
    create = 'create'
    assign = 'assign'
    unassign = 'unassign'
    reject = 'reject'
    accept = 'accept'
    unaccept = 'unaccept'
    transit = 'transit'
    activate = 'activate'
    complete = 'complete'
    fail = 'fail'
    cancel = 'cancel'
    assignee_near = 'assignee_near'
    assignee_away = 'assignee_away'
    updated = 'updated'


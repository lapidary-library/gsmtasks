# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import gsmtasks.components.schemas.Location.schema
import gsmtasks.components.schemas.TaskCommandTaskData.schema
import uuid


class TaskCommand(lapidary.runtime.ModelBase):
    task: str

    time: datetime.datetime

    action: str

    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    account: typing.Union[None, str] = None

    external_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    user: typing.Union[None, str] = None

    notes: typing.Union[None, str] = None

    location: typing.Union[None, gsmtasks.components.schemas.Location.schema.Location] = None

    assignee: typing.Union[None, str] = None

    state: typing.Union[None, str] = None

    error_message: typing.Union[None, str] = None

    task_data: typing.Union[None, gsmtasks.components.schemas.TaskCommandTaskData.schema.TaskCommandTaskData] = None

    accepted_at: typing.Union[None, datetime.datetime] = None

    rejected_at: typing.Union[None, datetime.datetime] = None

    created_at: typing.Union[None, datetime.datetime] = None

    updated_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

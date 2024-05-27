# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import gsmtasks.components.schemas.Location.schema
import gsmtasks.components.schemas.TaskCommandTaskData.schema
import lapidary.runtime
import uuid


class TaskCommand(lapidary.runtime.ModelBase):
    id: typing.Annotated[
        typing.Union[None, uuid.UUID],
        pydantic.Field(
            alias='id',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='url',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    account: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='account',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    task: typing.Annotated[
        str,
        pydantic.Field(
            alias='task',
        )
    ]

    time: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            alias='time',
        )
    ]

    ActionEnum: typing.Annotated[
        str,
        pydantic.Field(
            alias='ActionEnum',
        )
    ]

    user: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='user',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    created_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='created_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    updated_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='updated_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    external_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='external_id',
            max_length=100,
        )
    ] = None

    notes: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='notes',
        )
    ] = None

    location: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.Location.schema.Location],
        pydantic.Field(
            alias='location',
        )
    ] = None

    assignee: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='assignee',
        )
    ] = None

    TaskCommandStateEnum: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='TaskCommandStateEnum',
        )
    ] = None

    error_message: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='error_message',
        )
    ] = None

    TaskCommandTaskData: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.TaskCommandTaskData.schema.TaskCommandTaskData],
        pydantic.Field(
            alias='TaskCommandTaskData',
        )
    ] = None

    accepted_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='accepted_at',
        )
    ] = None

    rejected_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='rejected_at',
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
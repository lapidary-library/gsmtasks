# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import gsmtasks.components.schemas.TrackerTasks.schema
import gsmtasks.components.schemas.UserExport.schema
import lapidary.runtime
import uuid


class TrackerPublic(lapidary.runtime.ModelBase):
    id: typing.Annotated[
        typing.Union[None, uuid.UUID],
        pydantic.Field(
            alias='id',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    account: typing.Annotated[
        str,
        pydantic.Field(
            alias='account',
        )
    ]

    state: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='state',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    assignees: typing.Annotated[
        list[gsmtasks.components.schemas.UserExport.schema.UserExport],
        pydantic.Field(
            alias='assignees',
        )
    ]

    queue_positions: typing.Annotated[
        typing.Union[None, list[int]],
        pydantic.Field(
            alias='queue_positions',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    tasks: typing.Annotated[
        typing.Union[None, list[gsmtasks.components.schemas.TrackerTasks.schema.TrackerTasks]],
        pydantic.Field(
            alias='tasks',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    last_task_event_notes: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='last_task_event_notes',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    last_task_images: typing.Annotated[
        list[str],
        pydantic.Field(
            alias='last_task_images',
        )
    ]

    logo: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='logo',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    language: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='language',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    reviewed_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='reviewed_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    predicted_delivery: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='predicted_delivery',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    predicted_delivery_calculated_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='predicted_delivery_calculated_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    predicted_delivery_error: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='predicted_delivery_error',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    active_from: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='active_from',
        )
    ] = None

    active_until: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='active_until',
        )
    ] = None

    queued_states: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='queued_states',
        )
    ] = None

    active_states: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='active_states',
        )
    ] = None

    show_driver_info: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_driver_info',
        )
    ] = None

    show_destination: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_destination',
        )
    ] = None

    show_eta: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_eta',
        )
    ] = None

    show_sms_action: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_sms_action',
        )
    ] = None

    show_call_action: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_call_action',
        )
    ] = None

    show_predicted_delivery: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_predicted_delivery',
        )
    ] = None

    show_last_task_event_notes: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_last_task_event_notes',
        )
    ] = None

    show_last_task_images: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_last_task_images',
        )
    ] = None

    show_logo: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_logo',
        )
    ] = None

    show_path: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='show_path',
        )
    ] = None

    autozoom: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='autozoom',
        )
    ] = None

    max_zoom_level: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            alias='max_zoom_level',
            ge=-2147483648.0,
            le=2147483647.0,
        )
    ] = None

    reviews_allowed: typing.Annotated[
        typing.Union[None, bool],
        pydantic.Field(
            alias='reviews_allowed',
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
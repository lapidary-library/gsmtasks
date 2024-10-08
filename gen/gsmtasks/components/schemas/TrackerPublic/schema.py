# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import gsmtasks.components.schemas.TrackerTasks.schema
import gsmtasks.components.schemas.UserExport.schema
import uuid


class TrackerPublic(lapidary.runtime.ModelBase):
    account: str

    assignees: list[gsmtasks.components.schemas.UserExport.schema.UserExport]

    last_task_images: list[str]

    id: typing.Union[None, uuid.UUID] = None

    state: typing.Union[None, str] = None

    queue_positions: typing.Union[None, list[int]] = None

    tasks: typing.Union[None, list[gsmtasks.components.schemas.TrackerTasks.schema.TrackerTasks]] = None

    active_from: typing.Union[None, datetime.datetime] = None

    active_until: typing.Union[None, datetime.datetime] = None

    queued_states: typing.Union[None, list[str]] = None

    active_states: typing.Union[None, list[str]] = None

    show_driver_info: typing.Union[None, bool] = None

    show_destination: typing.Union[None, bool] = None

    show_eta: typing.Union[None, bool] = None

    show_sms_action: typing.Union[None, bool] = None

    show_call_action: typing.Union[None, bool] = None

    show_predicted_delivery: typing.Union[None, bool] = None

    show_last_task_event_notes: typing.Union[None, bool] = None

    show_last_task_images: typing.Union[None, bool] = None

    last_task_event_notes: typing.Union[None, str] = None

    logo: typing.Union[None, str] = None

    show_logo: typing.Union[None, bool] = None

    show_path: typing.Union[None, bool] = None

    autozoom: typing.Union[None, bool] = None

    max_zoom_level: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=-2147483648,
            le=2147483647,
        )
    ] = None

    language: typing.Union[None, str] = None

    reviews_allowed: typing.Union[None, bool] = None

    reviewed_at: typing.Union[None, datetime.datetime] = None

    predicted_delivery: typing.Union[None, datetime.datetime] = None

    predicted_delivery_calculated_at: typing.Union[None, datetime.datetime] = None

    predicted_delivery_error: typing.Union[None, str] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import uuid


class NotificationTemplate(lapidary.runtime.ModelBase):
    account: str

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
        )
    ]

    message: str

    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    event: typing.Union[None, str, typing.Any] = None

    state: typing.Union[None, str, typing.Any] = None

    task_category: typing.Union[None, str, typing.Any] = None

    scheduled_time_change: typing.Union[None, bool] = None

    recipient: typing.Union[None, str, typing.Any] = None

    emails: typing.Union[None, list[str]] = None

    phones: typing.Union[None, list[str]] = None

    via_sms: typing.Union[None, bool] = None

    via_email: typing.Union[None, bool] = None

    via_app: typing.Union[None, bool] = None

    is_active: typing.Union[None, bool] = None

    email_reply_to: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=254,
        )
    ] = None

    created_at: typing.Union[None, datetime.datetime] = None

    updated_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

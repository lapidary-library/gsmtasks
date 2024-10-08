# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import uuid


class Review(lapidary.runtime.ModelBase):
    tracker: str

    rating: typing.Annotated[
        int,
        pydantic.Field(
            ge=1,
            le=5,
        )
    ]

    id: typing.Union[None, uuid.UUID] = None

    account: typing.Union[None, str] = None

    comment: typing.Union[None, str] = None

    last_task: typing.Union[None, str] = None

    last_assignee: typing.Union[None, str] = None

    created_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

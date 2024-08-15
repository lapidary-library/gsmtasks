# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import decimal
import gsmtasks.components.schemas.Location.schema
import uuid


class TimeLocation(lapidary.runtime.ModelBase):
    time: datetime.datetime

    location: gsmtasks.components.schemas.Location.schema.Location

    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    source: typing.Union[None, str] = None

    user: typing.Union[None, str] = None

    is_moving: typing.Union[None, bool] = None

    event: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=20,
        )
    ] = None

    activity_type: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=20,
        )
    ] = None

    state: typing.Union[None, str] = None

    heading: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=-2147483648,
            le=2147483647,
        )
    ] = None

    speed: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=-2147483648,
            le=2147483647,
        )
    ] = None

    altitude: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=-2147483648,
            le=2147483647,
        )
    ] = None

    accuracy: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=-2147483648,
            le=2147483647,
        )
    ] = None

    battery_level: typing.Union[None, decimal.Decimal] = None

    created_at: typing.Union[None, datetime.datetime] = None

    updated_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

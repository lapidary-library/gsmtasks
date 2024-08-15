# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import uuid


class ClientRole(lapidary.runtime.ModelBase):
    account: str

    client: str

    user: str

    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    phone: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=128,
        )
    ] = None

    is_manager: typing.Union[None, bool] = None

    is_active: typing.Union[None, bool] = None

    created_at: typing.Union[None, datetime.datetime] = None

    updated_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

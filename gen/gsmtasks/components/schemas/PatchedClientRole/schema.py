# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing


class PatchedClientRole(lapidary.runtime.ModelBase):
    id: typing.Union[None, str] = None

    url: typing.Union[None, str] = None

    account: typing.Union[None, str] = None

    client: typing.Union[None, str] = None

    user: typing.Union[None, str] = None

    phone: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=128,
        )
    ] = None

    is_manager: typing.Union[None, bool] = None

    is_active: typing.Union[None, bool] = None

    created_at: typing.Union[None, str] = None

    updated_at: typing.Union[None, str] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

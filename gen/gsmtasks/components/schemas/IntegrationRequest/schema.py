# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing


class IntegrationRequest(lapidary.runtime.ModelBase):
    account: str

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=200,
        )
    ]

    id: typing.Union[None, str] = None

    notes: typing.Union[None, str] = None

    user: typing.Union[None, str] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing


class NestedContact(lapidary.runtime.ModelBase):
    name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=200,
        )
    ] = None

    company: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=200,
        )
    ] = None

    phones: typing.Union[None, list[str]] = None

    emails: typing.Union[None, list[str]] = None

    notes: typing.Union[None, str] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
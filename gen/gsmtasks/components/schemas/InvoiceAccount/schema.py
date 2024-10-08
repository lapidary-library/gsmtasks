# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import uuid


class InvoiceAccount(lapidary.runtime.ModelBase):
    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
        )
    ]

    id: typing.Union[None, uuid.UUID] = None

    slug: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            pattern=r'^[-a-zA-Z0-9_]+$',
        )
    ] = None

    registry_code: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=20,
        )
    ] = None

    vatin: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=20,
        )
    ] = None

    billing_reference: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=20,
        )
    ] = None

    billing_email: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=254,
        )
    ] = None

    billing_vat: typing.Union[None, bool] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

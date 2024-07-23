# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import uuid


class BraintreeCustomer(lapidary.runtime.ModelBase):
    account: str

    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    braintree_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=36,
        )
    ] = None

    first_name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=255,
        )
    ] = None

    last_name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=255,
        )
    ] = None

    company: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=255,
        )
    ] = None

    email: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=254,
        )
    ] = None

    phone: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=14,
        )
    ] = None

    website: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    vat: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=20,
        )
    ] = None

    payment_method_nonce: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=250,
        )
    ] = None

    created_at: typing.Union[None, datetime.datetime] = None

    updated_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
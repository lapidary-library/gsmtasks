# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import datetime
import lapidary.runtime
import uuid


class Email(lapidary.runtime.ModelBase):
    id: typing.Annotated[
        typing.Union[None, uuid.UUID],
        pydantic.Field(
            alias='id',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='url',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    account: typing.Annotated[
        str,
        pydantic.Field(
            alias='account',
        )
    ]

    state: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='state',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    notification: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='notification',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    sender: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='sender',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    subject: typing.Annotated[
        str,
        pydantic.Field(
            alias='subject',
            max_length=250,
        )
    ]

    message: typing.Annotated[
        str,
        pydantic.Field(
            alias='message',
        )
    ]

    sent_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='sent_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    failed_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='failed_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    received_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='received_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    created_at: typing.Annotated[
        typing.Union[None, datetime.datetime],
        pydantic.Field(
            alias='created_at',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    external_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='external_id',
            max_length=34,
        )
    ] = None

    from_email: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='from_email',
            max_length=254,
        )
    ] = None

    reply_to_email: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='reply_to_email',
            max_length=254,
        )
    ] = None

    to_emails: typing.Annotated[
        typing.Union[None, list[str]],
        pydantic.Field(
            alias='to_emails',
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
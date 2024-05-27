# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import gsmtasks.components.schemas.NestedAddress.schema
import lapidary.runtime
import uuid


class AuthenticatedUserCreate(lapidary.runtime.ModelBase):
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

    display_name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='display_name',
            direction=lapidary.runtime.ParamDirection.read,
        )
    ]

    email: typing.Annotated[
        str,
        pydantic.Field(
            alias='email',
        )
    ]

    first_name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='first_name',
            max_length=30,
        )
    ] = None

    last_name: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='last_name',
            max_length=30,
        )
    ] = None

    phone: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='phone',
            max_length=128,
        )
    ] = None

    password: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='password',
            direction=lapidary.runtime.ParamDirection.write,
        )
    ] = None

    NestedAddress: typing.Annotated[
        typing.Union[None, gsmtasks.components.schemas.NestedAddress.schema.NestedAddress],
        pydantic.Field(
            alias='NestedAddress',
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
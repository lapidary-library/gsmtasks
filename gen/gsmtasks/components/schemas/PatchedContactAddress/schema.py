# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import gsmtasks.components.schemas.NestedAddress.schema
import gsmtasks.components.schemas.NestedContact.schema
import uuid


class PatchedContactAddress(lapidary.runtime.ModelBase):
    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    external_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    account: typing.Union[None, str] = None

    client: typing.Union[None, str] = None

    contact: typing.Union[None, gsmtasks.components.schemas.NestedContact.schema.NestedContact] = None

    address: typing.Union[None, gsmtasks.components.schemas.NestedAddress.schema.NestedAddress] = None

    is_orderer: typing.Union[None, bool] = None

    is_receiver: typing.Union[None, bool] = None

    source: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    created_at: typing.Union[None, datetime.datetime] = None

    updated_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import gsmtasks.components.schemas.OrderData.properties.orderer.schema


class OrderData(lapidary.runtime.ModelBase):
    auto_assign: typing.Union[None, bool] = None

    description: typing.Union[None, str] = None

    reference: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    client: typing.Union[None, str] = None

    orderer: typing.Union[None, gsmtasks.components.schemas.OrderData.properties.orderer.schema.orderer] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import typing

import lapidary.runtime
import pydantic
import typing_extensions
import lapidary.runtime


class AccountStripeSetupIntentsGet(lapidary.runtime.ModelBase):
    payment_method_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            alias='payment_method_id',
            max_length=100,
        )
    ] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
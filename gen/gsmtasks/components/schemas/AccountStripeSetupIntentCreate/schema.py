# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing


class AccountStripeSetupIntentCreate(lapidary.runtime.ModelBase):
    payment_method_id: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
        )
    ]

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

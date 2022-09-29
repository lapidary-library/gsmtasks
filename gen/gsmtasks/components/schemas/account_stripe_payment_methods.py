from __future__ import annotations

import typing
import lapidary_base
import pydantic
class AccountStripePaymentMethods(pydantic.BaseModel):
    default_payment_method_id: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

AccountStripePaymentMethods.update_forward_refs()

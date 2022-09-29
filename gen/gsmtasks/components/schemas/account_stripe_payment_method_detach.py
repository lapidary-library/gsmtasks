from __future__ import annotations

import typing
import lapidary_base
import pydantic
class AccountStripePaymentMethodDetach(pydantic.BaseModel):
    stripe_payment_method_id: typing.Annotated[
        str,
        pydantic.Field(
            max_length=255,
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

AccountStripePaymentMethodDetach.update_forward_refs()

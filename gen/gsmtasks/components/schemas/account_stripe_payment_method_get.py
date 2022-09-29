from __future__ import annotations

import typing
import lapidary_base
import pydantic


class AccountStripePaymentMethodGet(pydantic.BaseModel):
    payment_method_id: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


AccountStripePaymentMethodGet.update_forward_refs()

from __future__ import annotations

import typing
import lapidary_base
import pydantic
class AccountStripeSetupAttemptGet(pydantic.BaseModel):
    setup_attempt_id: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

AccountStripeSetupAttemptGet.update_forward_refs()

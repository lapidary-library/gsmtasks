from __future__ import annotations

import typing
import lapidary_base
import pydantic


class AccountStripeSetupIntentGet(pydantic.BaseModel):
    setup_intent_id: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


AccountStripeSetupIntentGet.update_forward_refs()

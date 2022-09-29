from __future__ import annotations

import typing
import lapidary_base
import pydantic
import lapidary_base.absent


class AccountStripeSetupIntentsGet(pydantic.BaseModel):
    payment_method_id: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=100,
        ),
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


AccountStripeSetupIntentsGet.update_forward_refs()

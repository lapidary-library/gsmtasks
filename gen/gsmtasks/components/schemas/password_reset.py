from __future__ import annotations

import typing
import lapidary_base
import pydantic
class PasswordReset(pydantic.BaseModel):
    email: typing.Annotated[
        str,
        pydantic.Field(
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

PasswordReset.update_forward_refs()

from __future__ import annotations

import typing
import lapidary_base
import pydantic
class AuthToken(pydantic.BaseModel):
    username: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.write,
        )
    ]

    password: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.write,
        )
    ]

    token: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

AuthToken.update_forward_refs()

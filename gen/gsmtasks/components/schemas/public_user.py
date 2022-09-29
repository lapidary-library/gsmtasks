from __future__ import annotations

import typing
import lapidary_base
import pydantic
import uuid
class PublicUser(pydantic.BaseModel):
    id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    url: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    display_name: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    email: typing.Annotated[
        str,
        pydantic.Field(
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

PublicUser.update_forward_refs()

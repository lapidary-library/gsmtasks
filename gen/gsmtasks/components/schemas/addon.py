from __future__ import annotations

import typing
import lapidary_base
import pydantic
import uuid


class Addon(pydantic.BaseModel):
    id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
        ),
    ]

    short_description: typing.Annotated[str, pydantic.Field()]

    description: typing.Annotated[str, pydantic.Field()]

    price: typing.Annotated[
        str,
        pydantic.Field(
            max_length=50,
        ),
    ]

    unit: typing.Annotated[
        str,
        pydantic.Field(
            max_length=50,
        ),
    ]

    icon: typing.Annotated[str, pydantic.Field()]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


Addon.update_forward_refs()

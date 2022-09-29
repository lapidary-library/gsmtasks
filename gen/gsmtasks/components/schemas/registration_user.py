from __future__ import annotations

import typing
import lapidary_base
import pydantic
import lapidary_base.absent
import uuid


class RegistrationUser(pydantic.BaseModel):
    id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    url: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    name: typing.Annotated[str, pydantic.Field()]

    email: typing.Annotated[str, pydantic.Field()]

    phone: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=128,
        ),
    ] = lapidary_base.absent.ABSENT

    password: typing.Annotated[
        str,
        pydantic.Field(
            min_length=6,
            max_length=100,
            direction=lapidary_base.ParamDirection.write,
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


RegistrationUser.update_forward_refs()

from __future__ import annotations

import typing
import lapidary_base
import pydantic
import lapidary_base.absent
import uuid


class UserActivation(pydantic.BaseModel):
    token: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.write,
        ),
    ]

    password: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.write,
        ),
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


UserActivation.update_forward_refs()

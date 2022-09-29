from __future__ import annotations

import typing
import lapidary_base
import pydantic
import enum
import lapidary_base.absent
import uuid


class UsersActivateCreateFormat(enum.Enum):
    json = "json"
    xml = "xml"


class UsersActivateCreate(pydantic.BaseModel):
    q_format: typing.Annotated[
        typing.Union[
            UsersActivateCreateFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="format",
        ),
    ] = lapidary_base.absent.ABSENT

    p_id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.path,
            alias="id",
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


UsersActivateCreate.update_forward_refs()

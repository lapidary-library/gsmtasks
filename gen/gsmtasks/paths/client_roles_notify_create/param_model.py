from __future__ import annotations

import typing
import lapidary_base
import pydantic
import enum
import lapidary_base.absent
import uuid
class ClientRolesNotifyCreateFormat(enum.Enum):
    json = 'json'
    xlsx = 'xlsx'

class ClientRolesNotifyCreate(pydantic.BaseModel):
    q_format: typing.Annotated[
        typing.Union[
            ClientRolesNotifyCreateFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='format',
        )
    ] = lapidary_base.absent.ABSENT

    p_id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.path,
            alias='id',
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

ClientRolesNotifyCreate.update_forward_refs()

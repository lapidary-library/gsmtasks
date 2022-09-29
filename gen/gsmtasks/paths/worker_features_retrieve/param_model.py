from __future__ import annotations

import typing
import lapidary_base
import pydantic
import enum
import lapidary_base.absent
import uuid
class WorkerFeaturesRetrieveFormat(enum.Enum):
    json = 'json'
    xlsx = 'xlsx'

class WorkerFeaturesRetrieve(pydantic.BaseModel):
    q_format: typing.Annotated[
        typing.Union[
            WorkerFeaturesRetrieveFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='format',
        )
    ] = lapidary_base.absent.ABSENT

    p_user_id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.path,
            alias='user_id',
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

WorkerFeaturesRetrieve.update_forward_refs()

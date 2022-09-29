from __future__ import annotations

import typing
import lapidary_base
import pydantic
import enum
import lapidary_base.absent
class DevicesCreateFormat(enum.Enum):
    json = 'json'
    xlsx = 'xlsx'

class DevicesCreate(pydantic.BaseModel):
    q_format: typing.Annotated[
        typing.Union[
            DevicesCreateFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='format',
        )
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

DevicesCreate.update_forward_refs()

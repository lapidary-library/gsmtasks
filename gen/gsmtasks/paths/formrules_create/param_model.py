from __future__ import annotations

import typing
import lapidary_base
import pydantic
import enum
import lapidary_base.absent
class FormrulesCreateFormat(enum.Enum):
    json = 'json'
    xlsx = 'xlsx'

class FormrulesCreate(pydantic.BaseModel):
    q_format: typing.Annotated[
        typing.Union[
            FormrulesCreateFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='format',
        )
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

FormrulesCreate.update_forward_refs()

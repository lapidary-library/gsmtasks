from __future__ import annotations

import typing
import lapidary_base
import pydantic
import enum
import lapidary_base.absent


class ClientRolesCreateFormat(enum.Enum):
    json = "json"
    xlsx = "xlsx"


class ClientRolesCreate(pydantic.BaseModel):
    q_format: typing.Annotated[
        typing.Union[
            ClientRolesCreateFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="format",
        ),
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


ClientRolesCreate.update_forward_refs()

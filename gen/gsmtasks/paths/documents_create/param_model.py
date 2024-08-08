# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import enum
import lapidary.runtime.absent


class DocumentsCreateFormat(enum.Enum):
    json = "json"
    xlsx = "xlsx"


class DocumentsCreate(pydantic.BaseModel):
    q_format: typing.Annotated[
        typing.Union[
            DocumentsCreateFormat,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            alias="format",
            in_=lapidary.runtime.ParamPlacement.query,
        ),
    ] = lapidary.runtime.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


DocumentsCreate.update_forward_refs()
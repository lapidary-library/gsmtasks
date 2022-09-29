from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.import_mapping_line
import uuid
class ImportMapping(pydantic.BaseModel):
    id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    url: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    account: typing.Annotated[
        str,
        pydantic.Field(
        )
    ]

    field_names: typing.Annotated[
        list[
            str,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.write,
        )
    ]

    lines: typing.Annotated[
        list[
            gsmtasks.components.schemas.import_mapping_line.ImportMappingLine,
        ],
        pydantic.Field(
        )
    ]

    created_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

ImportMapping.update_forward_refs()

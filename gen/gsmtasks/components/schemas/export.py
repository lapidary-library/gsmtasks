from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.export_model_enum
import gsmtasks.components.schemas.format_enum
import lapidary_base.absent
import uuid
class Export(pydantic.BaseModel):
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

    export_model: typing.Annotated[
        gsmtasks.components.schemas.export_model_enum.ExportModelEnum,
        pydantic.Field(
        )
    ]

    field_names: typing.Annotated[
        typing.Union[
            list[
            str,
        ],
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    format: typing.Annotated[
        gsmtasks.components.schemas.format_enum.FormatEnum,
        pydantic.Field(
        )
    ]

    link: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    created_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    updated_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

Export.update_forward_refs()

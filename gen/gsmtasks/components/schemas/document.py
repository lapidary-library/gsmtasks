from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.blank_enum
import gsmtasks.components.schemas.null_enum
import gsmtasks.components.schemas.source_enum
import lapidary_base.absent
import uuid


class Document(pydantic.BaseModel):
    id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    url: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    account: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    external_id: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=100,
        ),
    ] = lapidary_base.absent.ABSENT

    order: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    task: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    file_upload: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.write,
        ),
    ] = lapidary_base.absent.ABSENT

    file: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    file_name: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    mimetype: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    thumbnail: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    description: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    created_by: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    source: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.source_enum.SourceEnum,
            gsmtasks.components.schemas.blank_enum.BlankEnum,
            gsmtasks.components.schemas.null_enum.NullEnum,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    visible_to_worker: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    visible_to_client: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    created_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    updated_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


Document.update_forward_refs()

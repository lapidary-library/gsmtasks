from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.blank_enum
import gsmtasks.components.schemas.nested_contact
import gsmtasks.components.schemas.null_enum
import gsmtasks.components.schemas.source_enum
import lapidary_base.absent
import uuid
class Signature(pydantic.BaseModel):
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
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    task: typing.Annotated[
        str,
        pydantic.Field(
        )
    ]

    file_upload: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.write,
        )
    ]

    file: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    file_name: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    mimetype: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    thumbnail: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    signer: typing.Annotated[
        gsmtasks.components.schemas.nested_contact.NestedContact,
        pydantic.Field(
        )
    ]

    documents: typing.Annotated[
        typing.Union[
            list[
            str,
        ],
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    location: typing.Annotated[
        typing.Union[
            typing.Any,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    created_by: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    source: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.source_enum.SourceEnum,
            gsmtasks.components.schemas.blank_enum.BlankEnum,
            gsmtasks.components.schemas.null_enum.NullEnum,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

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

Signature.update_forward_refs()

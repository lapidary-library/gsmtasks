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


class S3FileUploadS3Signature(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class S3FileUpload(pydantic.BaseModel):
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

    file: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    file_name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
            direction=lapidary_base.ParamDirection.write,
        ),
    ]

    file_type: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
            direction=lapidary_base.ParamDirection.write,
        ),
    ]

    s3_signature: typing.Annotated[
        typing.Union[
            S3FileUploadS3Signature,
            None,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

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


S3FileUploadS3Signature.update_forward_refs()
S3FileUpload.update_forward_refs()

from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import enum
import lapidary_base.absent
import uuid


class FileUploadsListFormat(enum.Enum):
    json = "json"
    xlsx = "xlsx"


class FileUploadsListSource(enum.Enum):
    web = "web"
    mobile = "mobile"
    integration = "integration"


class FileUploadsList(pydantic.BaseModel):
    q_created_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="created_at__date",
        ),
    ] = lapidary_base.absent.ABSENT

    q_created_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="created_at__date_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_created_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="created_at__gt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_created_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="created_at__gt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_created_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="created_at__gte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_created_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="created_at__gte_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_created_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="created_at__lt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_created_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="created_at__lt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_created_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="created_at__lte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_created_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="created_at__lte_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_created_by: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="created_by",
        ),
    ] = lapidary_base.absent.ABSENT

    q_created_by__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="created_by__in",
        ),
    ] = lapidary_base.absent.ABSENT

    q_cursor: typing.Annotated[
        typing.Union[
            int,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="cursor",
        ),
    ] = lapidary_base.absent.ABSENT

    q_filename: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="filename",
        ),
    ] = lapidary_base.absent.ABSENT

    q_filename__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="filename__icontains",
        ),
    ] = lapidary_base.absent.ABSENT

    q_filename__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="filename__iexact",
        ),
    ] = lapidary_base.absent.ABSENT

    q_filename__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="filename__iregex",
        ),
    ] = lapidary_base.absent.ABSENT

    q_filename__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="filename__istartswith",
        ),
    ] = lapidary_base.absent.ABSENT

    q_filename__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="filename__search",
        ),
    ] = lapidary_base.absent.ABSENT

    q_format: typing.Annotated[
        typing.Union[
            FileUploadsListFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="format",
        ),
    ] = lapidary_base.absent.ABSENT

    q_ordering: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="ordering",
        ),
    ] = lapidary_base.absent.ABSENT

    q_page_size: typing.Annotated[
        typing.Union[
            int,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="page_size",
        ),
    ] = lapidary_base.absent.ABSENT

    q_source: typing.Annotated[
        typing.Union[
            FileUploadsListSource,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="source",
        ),
    ] = lapidary_base.absent.ABSENT

    q_updated_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="updated_at__date",
        ),
    ] = lapidary_base.absent.ABSENT

    q_updated_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="updated_at__date_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_updated_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="updated_at__gt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_updated_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="updated_at__gt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_updated_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="updated_at__gte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_updated_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="updated_at__gte_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_updated_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="updated_at__lt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_updated_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="updated_at__lt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_updated_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="updated_at__lte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_updated_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="updated_at__lte_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


FileUploadsList.update_forward_refs()

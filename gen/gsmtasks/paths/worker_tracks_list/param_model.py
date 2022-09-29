from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import enum
import lapidary_base.absent


class WorkerTracksListFormat(enum.Enum):
    json = "json"
    xlsx = "xlsx"


class WorkerTracksList(pydantic.BaseModel):
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

    q_end_time__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="end_time__date",
        ),
    ] = lapidary_base.absent.ABSENT

    q_end_time__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="end_time__date_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_end_time__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="end_time__gt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_end_time__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="end_time__gt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_end_time__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="end_time__gte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_end_time__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="end_time__gte_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_end_time__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="end_time__lt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_end_time__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="end_time__lt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_end_time__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="end_time__lte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_end_time__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="end_time__lte_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_format: typing.Annotated[
        typing.Union[
            WorkerTracksListFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="format",
        ),
    ] = lapidary_base.absent.ABSENT

    q_start_time__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="start_time__date",
        ),
    ] = lapidary_base.absent.ABSENT

    q_start_time__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="start_time__date_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_start_time__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="start_time__gt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_start_time__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="start_time__gt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_start_time__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="start_time__gte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_start_time__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="start_time__gte_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_start_time__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="start_time__lt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_start_time__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="start_time__lt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_start_time__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="start_time__lte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_start_time__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="start_time__lte_or_isnull",
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


WorkerTracksList.update_forward_refs()

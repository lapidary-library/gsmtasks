from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import enum
import lapidary_base.absent


class TaskAddressFeaturesListCategory(enum.Enum):
    assignment = "assignment"
    pick_up = "pick_up"
    drop_off = "drop_off"
    warehouse = "warehouse"


class TaskAddressFeaturesListFormat(enum.Enum):
    json = "json"
    xlsx = "xlsx"


class TaskAddressFeaturesList(pydantic.BaseModel):
    q_account: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="account",
        ),
    ] = lapidary_base.absent.ABSENT

    q_assignee: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="assignee",
        ),
    ] = lapidary_base.absent.ABSENT

    q_category: typing.Annotated[
        typing.Union[
            TaskAddressFeaturesListCategory,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="category",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_after__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_after__date",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_after__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_after__date_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_after__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_after__gt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_after__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_after__gt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_after__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_after__gte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_after__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_after__gte_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_after__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_after__lt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_after__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_after__lt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_after__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_after__lte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_after__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_after__lte_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_before__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_before__date",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_before__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_before__date_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_before__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_before__gt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_before__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_before__gt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_before__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_before__gte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_before__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_before__gte_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_before__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_before__lt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_before__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_before__lt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_before__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_before__lte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_complete_before__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="complete_before__lte_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

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

    q_format: typing.Annotated[
        typing.Union[
            TaskAddressFeaturesListFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="format",
        ),
    ] = lapidary_base.absent.ABSENT

    q_owner: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="owner",
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

    q_position__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="position__date",
        ),
    ] = lapidary_base.absent.ABSENT

    q_position__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="position__date_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_position__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="position__gt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_position__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="position__gt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_position__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="position__gte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_position__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="position__gte_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_position__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="position__lt",
        ),
    ] = lapidary_base.absent.ABSENT

    q_position__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="position__lt_or_isnull",
        ),
    ] = lapidary_base.absent.ABSENT

    q_position__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="position__lte",
        ),
    ] = lapidary_base.absent.ABSENT

    q_position__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias="position__lte_or_isnull",
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


TaskAddressFeaturesList.update_forward_refs()

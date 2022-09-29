from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.null_enum
import gsmtasks.components.schemas.objective_enum
import lapidary_base.absent
import uuid


class RouteOptimizationSerializerV2TotalDuration(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class RouteOptimizationSerializerV2(pydantic.BaseModel):
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

    account: typing.Annotated[str, pydantic.Field()]

    assignees: typing.Annotated[
        list[
            str,
        ],
        pydantic.Field(),
    ]

    state: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    objective: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.objective_enum.ObjectiveEnum,
            gsmtasks.components.schemas.null_enum.NullEnum,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    tasks: typing.Annotated[
        list[
            str,
        ],
        pydantic.Field(),
    ]

    start_time: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    start_location: typing.Annotated[
        typing.Union[
            typing.Any,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    end_location: typing.Annotated[
        typing.Union[
            typing.Any,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    unassign_not_optimal: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    total_distance: typing.Annotated[
        int,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    total_duration: typing.Annotated[
        RouteOptimizationSerializerV2TotalDuration,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    commit: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    created_by: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    commited_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    scheduled_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    started_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    ready_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    completed_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    failed_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

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

    errors: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


RouteOptimizationSerializerV2TotalDuration.update_forward_refs()
RouteOptimizationSerializerV2.update_forward_refs()

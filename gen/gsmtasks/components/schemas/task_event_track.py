from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import lapidary_base.absent
import uuid


class TaskEventTrack(pydantic.BaseModel):
    id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    model: typing.Annotated[
        str,
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

    task: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    task_event: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    event: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    from_state: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    to_state: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    user: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    notes: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    assignee: typing.Annotated[
        typing.Union[
            uuid.UUID,
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

    track: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


TaskEventTrack.update_forward_refs()

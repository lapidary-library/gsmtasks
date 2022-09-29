from __future__ import annotations

import typing
import lapidary_base
import pydantic
class TasksStatesCount(pydantic.BaseModel):
    unassigned: typing.Annotated[
        int,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    assigned: typing.Annotated[
        int,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    accepted: typing.Annotated[
        int,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    transit: typing.Annotated[
        int,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    active: typing.Annotated[
        int,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    completed: typing.Annotated[
        int,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    failed: typing.Annotated[
        int,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    cancelled: typing.Annotated[
        int,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

TasksStatesCount.update_forward_refs()

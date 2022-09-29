from __future__ import annotations

import typing
import lapidary_base
import pydantic


class TasksStatesCountResponseDates(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class TasksStatesCountResponse(pydantic.BaseModel):
    dates: typing.Annotated[
        TasksStatesCountResponseDates,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


TasksStatesCountResponseDates.update_forward_refs()
TasksStatesCountResponse.update_forward_refs()

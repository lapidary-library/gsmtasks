from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.location
import uuid


class WorkerTrack(pydantic.BaseModel):
    id: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    track: typing.Annotated[
        gsmtasks.components.schemas.location.Location, pydantic.Field()
    ]

    user: typing.Annotated[uuid.UUID, pydantic.Field()]

    start_time: typing.Annotated[datetime.datetime, pydantic.Field()]

    end_time: typing.Annotated[datetime.datetime, pydantic.Field()]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


WorkerTrack.update_forward_refs()

from __future__ import annotations

import typing
import lapidary_base
import pydantic
import lapidary_base.absent


class TaskAssign(pydantic.BaseModel):
    notes: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    location: typing.Annotated[
        typing.Union[
            typing.Any,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    assignee: typing.Annotated[str, pydantic.Field()]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


TaskAssign.update_forward_refs()

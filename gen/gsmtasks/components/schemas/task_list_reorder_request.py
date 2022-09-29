from __future__ import annotations

import typing
import lapidary_base
import pydantic


class TaskListReorderRequest(pydantic.BaseModel):
    account: typing.Annotated[str, pydantic.Field()]

    assignee: typing.Annotated[
        typing.Union[
            str,
            None,
        ],
        pydantic.Field(),
    ]

    assign_tasks: typing.Annotated[
        list[
            str,
        ],
        pydantic.Field(),
    ]

    reorder_tasks: typing.Annotated[
        list[
            str,
        ],
        pydantic.Field(),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


TaskListReorderRequest.update_forward_refs()

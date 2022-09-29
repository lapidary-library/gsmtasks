from __future__ import annotations

import typing
import lapidary_base
import pydantic
import gsmtasks.components.schemas.client
import gsmtasks.components.schemas.order
import gsmtasks.components.schemas.readable_user
import gsmtasks.components.schemas.recurrence
import gsmtasks.components.schemas.task
class RecurrenceListScene(pydantic.BaseModel):
    clients: typing.Annotated[
        list[
            gsmtasks.components.schemas.client.Client,
        ],
        pydantic.Field(
        )
    ]

    orders: typing.Annotated[
        list[
            gsmtasks.components.schemas.order.Order,
        ],
        pydantic.Field(
        )
    ]

    tasks: typing.Annotated[
        list[
            gsmtasks.components.schemas.task.Task,
        ],
        pydantic.Field(
        )
    ]

    assignees: typing.Annotated[
        list[
            gsmtasks.components.schemas.readable_user.ReadableUser,
        ],
        pydantic.Field(
        )
    ]

    recurrences: typing.Annotated[
        list[
            gsmtasks.components.schemas.recurrence.Recurrence,
        ],
        pydantic.Field(
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

RecurrenceListScene.update_forward_refs()

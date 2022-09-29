from __future__ import annotations

import typing
import lapidary_base
import pydantic
import gsmtasks.components.schemas.location
import gsmtasks.components.schemas.task_category_enum
import gsmtasks.components.schemas.task_state_enum
import lapidary_base.absent
import uuid
class TaskAddressFeature(pydantic.BaseModel):
    model: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    task: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    formatted_address: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    category: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.task_category_enum.TaskCategoryEnum,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    state: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.task_state_enum.TaskStateEnum,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    geometry: typing.Annotated[
        gsmtasks.components.schemas.location.Location,
        pydantic.Field(
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

TaskAddressFeature.update_forward_refs()

from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.account_user
import gsmtasks.components.schemas.legacy_task
import gsmtasks.components.schemas.order
import gsmtasks.components.schemas.task_metadata
import gsmtasks.components.schemas.worker_feature
class DashboardSceneAssignedTaskCounts(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class DashboardScene(pydantic.BaseModel):
    orders: typing.Annotated[
        list[
            gsmtasks.components.schemas.order.Order,
        ],
        pydantic.Field(
        )
    ]

    tasks: typing.Annotated[
        list[
            gsmtasks.components.schemas.legacy_task.LegacyTask,
        ],
        pydantic.Field(
        )
    ]

    task_metadatas: typing.Annotated[
        list[
            gsmtasks.components.schemas.task_metadata.TaskMetadata,
        ],
        pydantic.Field(
        )
    ]

    assigned_task_counts: typing.Annotated[
        DashboardSceneAssignedTaskCounts,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    workers: typing.Annotated[
        list[
            gsmtasks.components.schemas.account_user.AccountUser,
        ],
        pydantic.Field(
        )
    ]

    worker_features: typing.Annotated[
        list[
            gsmtasks.components.schemas.worker_feature.WorkerFeature,
        ],
        pydantic.Field(
        )
    ]

    updated_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

DashboardSceneAssignedTaskCounts.update_forward_refs()
DashboardScene.update_forward_refs()

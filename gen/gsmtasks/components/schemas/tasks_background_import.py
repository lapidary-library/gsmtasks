from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import lapidary_base.absent
import uuid


class TasksBackgroundImportTasksDataItem(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class TasksBackgroundImportErrors(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class TasksBackgroundImport(pydantic.BaseModel):
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

    mapping: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    created_by: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    tasks_data: typing.Annotated[
        list[
            TasksBackgroundImportTasksDataItem,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.write,
        ),
    ]

    state: typing.Annotated[
        typing.Any,
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

    errors: typing.Annotated[
        typing.Union[
            TasksBackgroundImportErrors,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    celery_task_id: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=50,
        ),
    ] = lapidary_base.absent.ABSENT

    tasks_created: typing.Annotated[
        list[
            str,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    assignees: typing.Annotated[
        list[
            str,
        ],
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

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


TasksBackgroundImportTasksDataItem.update_forward_refs()
TasksBackgroundImportErrors.update_forward_refs()
TasksBackgroundImport.update_forward_refs()

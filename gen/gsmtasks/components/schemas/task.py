from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.nested_address
import gsmtasks.components.schemas.nested_contact
import gsmtasks.components.schemas.task_category_enum
import lapidary_base.absent
import uuid
class TaskDuration(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class TaskMetafields(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class TaskForms(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class TaskActions(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class TaskCounts(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class Task(pydantic.BaseModel):
    id: typing.Annotated[
        typing.Union[
            uuid.UUID,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    url: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    account: typing.Annotated[
        str,
        pydantic.Field(
        )
    ]

    order: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    route: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    order_reference: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    external_id: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=100,
        )
    ] = lapidary_base.absent.ABSENT

    category: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.task_category_enum.TaskCategoryEnum,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    orderer: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    orderer_name: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    receiver: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    contact: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.nested_contact.NestedContact,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    address: typing.Annotated[
        gsmtasks.components.schemas.nested_address.NestedAddress,
        pydantic.Field(
        )
    ]

    description: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    reference: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=100,
        )
    ] = lapidary_base.absent.ABSENT

    complete_after: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    complete_before: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    scheduled_time: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    state: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    completed_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    cancelled_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    assignee: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    auto_assign: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    assignee_proximity: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    position: typing.Annotated[
        typing.Union[
            float,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=0.0,
            le=253402300799.0,
        )
    ] = lapidary_base.absent.ABSENT

    priority: typing.Annotated[
        typing.Union[
            int,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=-2147483648.0,
            le=2147483647.0,
        )
    ] = lapidary_base.absent.ABSENT

    duration: typing.Annotated[
        typing.Union[
            TaskDuration,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    size: typing.Annotated[
        typing.Union[
            list[
            int,
        ],
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    is_full_load: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    metafields: typing.Annotated[
        typing.Union[
            TaskMetafields,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    forms: typing.Annotated[
        TaskForms,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    created_by: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    issues: typing.Annotated[
        list[
            str,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    created_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    updated_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    events: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    documents: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    signatures: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    actions: typing.Annotated[
        TaskActions,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    counts: typing.Annotated[
        TaskCounts,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

TaskDuration.update_forward_refs()
TaskMetafields.update_forward_refs()
TaskForms.update_forward_refs()
TaskActions.update_forward_refs()
TaskCounts.update_forward_refs()
Task.update_forward_refs()

from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.assignee_proximity_enum
import gsmtasks.components.schemas.blank_enum
import gsmtasks.components.schemas.event_enum
import gsmtasks.components.schemas.null_enum
import gsmtasks.components.schemas.recipient_enum
import gsmtasks.components.schemas.task_state_enum
import lapidary_base.absent
import uuid
class Notification(pydantic.BaseModel):
    id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    url: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    method: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    task: typing.Annotated[
        str,
        pydantic.Field(
        )
    ]

    template: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    event: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.event_enum.EventEnum,
            gsmtasks.components.schemas.blank_enum.BlankEnum,
            gsmtasks.components.schemas.null_enum.NullEnum,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    state: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.task_state_enum.TaskStateEnum,
            gsmtasks.components.schemas.blank_enum.BlankEnum,
            gsmtasks.components.schemas.null_enum.NullEnum,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    assignee_proximity: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.assignee_proximity_enum.AssigneeProximityEnum,
            gsmtasks.components.schemas.blank_enum.BlankEnum,
            gsmtasks.components.schemas.null_enum.NullEnum,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    recipient: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.recipient_enum.RecipientEnum,
            gsmtasks.components.schemas.blank_enum.BlankEnum,
            gsmtasks.components.schemas.null_enum.NullEnum,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    emails: typing.Annotated[
        typing.Union[
            list[
            str,
        ],
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    phones: typing.Annotated[
        typing.Union[
            list[
            str,
        ],
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    message: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    add_tracking_link: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    sms_count: typing.Annotated[
        int,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    sent_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    via_app: typing.Annotated[
        bool,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    via_email: typing.Annotated[
        bool,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    via_sms: typing.Annotated[
        bool,
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

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

Notification.update_forward_refs()

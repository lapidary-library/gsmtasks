from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.task_state_enum
import lapidary_base.absent
import uuid
class Tracker(pydantic.BaseModel):
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

    account: typing.Annotated[
        str,
        pydantic.Field(
        )
    ]

    tasks: typing.Annotated[
        list[
            str,
        ],
        pydantic.Field(
        )
    ]

    active_from: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    active_until: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    queued_states: typing.Annotated[
        typing.Union[
            list[
            gsmtasks.components.schemas.task_state_enum.TaskStateEnum,
        ],
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    active_states: typing.Annotated[
        typing.Union[
            list[
            gsmtasks.components.schemas.task_state_enum.TaskStateEnum,
        ],
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    show_driver_info: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    show_destination: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    show_eta: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    show_sms_action: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    show_call_action: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    show_logo: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    show_path: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    show_predicted_delivery: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    autozoom: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    max_zoom_level: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=-2147483648.0,
            le=2147483647.0,
        )
    ] = lapidary_base.absent.ABSENT

    tracking_page_url: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    reviews_allowed: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    reviewed_at: typing.Annotated[
        datetime.datetime,
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

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

Tracker.update_forward_refs()

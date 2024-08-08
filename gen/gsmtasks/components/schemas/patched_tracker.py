# Generated by Lapidary.
# All manual changes will be lost!

from __future__ import annotations

import typing
import lapidary.runtime
import pydantic
import datetime
import gsmtasks.components.schemas.task_state_enum
import lapidary.runtime.absent
import uuid


class PatchedTracker(pydantic.BaseModel):
    id: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    url: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    account: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    tasks: typing.Annotated[
        typing.Union[
            list[
                str,
            ],
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    active_from: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    active_until: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    queued_states: typing.Annotated[
        typing.Union[
            list[
                gsmtasks.components.schemas.task_state_enum.TaskStateEnum,
            ],
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    active_states: typing.Annotated[
        typing.Union[
            list[
                gsmtasks.components.schemas.task_state_enum.TaskStateEnum,
            ],
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    show_driver_info: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    show_destination: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    show_eta: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    show_sms_action: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    show_call_action: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    show_logo: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    show_path: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    show_predicted_delivery: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    autozoom: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    max_zoom_level: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            ge=-2147483648.0,
            le=2147483647.0,
        ),
    ] = lapidary.runtime.absent.ABSENT

    tracking_page_url: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    reviews_allowed: typing.Annotated[
        typing.Union[
            bool,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary.runtime.absent.ABSENT

    reviewed_at: typing.Annotated[
        typing.Union[
            datetime.datetime,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    created_by: typing.Annotated[
        typing.Union[
            str,
            lapidary.runtime.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary.runtime.ParamDirection.read,
        ),
    ] = lapidary.runtime.absent.ABSENT

    class Config(pydantic.BaseConfig):
        use_enum_values = True
        extra = pydantic.Extra.allow


PatchedTracker.update_forward_refs()
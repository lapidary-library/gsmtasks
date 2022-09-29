from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.mode_enum
import gsmtasks.components.schemas.status_enum
import lapidary_base.absent


class WorkingState(pydantic.BaseModel):
    account_role: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    account: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    user: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    mode: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.mode_enum.ModeEnum,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    timestamp: typing.Annotated[
        typing.Union[
            datetime.datetime,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    status: typing.Annotated[
        gsmtasks.components.schemas.status_enum.StatusEnum, pydantic.Field()
    ]

    created_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


WorkingState.update_forward_refs()

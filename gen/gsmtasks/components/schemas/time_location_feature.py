from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.location
import gsmtasks.components.schemas.time_location_state_enum
import lapidary_base.absent
import uuid


class TimeLocationFeature(pydantic.BaseModel):
    model: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    source: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    user: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    time: typing.Annotated[datetime.datetime, pydantic.Field()]

    state: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.time_location_state_enum.TimeLocationStateEnum,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    heading: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=-2147483648.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    speed: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=-2147483648.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    altitude: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=-2147483648.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    accuracy: typing.Annotated[
        typing.Union[
            int,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=-2147483648.0,
            le=2147483647.0,
        ),
    ] = lapidary_base.absent.ABSENT

    battery_level: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            regex=r"^-?\d{0,1}(?:\.\d{0,3})?$",
        ),
    ] = lapidary_base.absent.ABSENT

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

    location: typing.Annotated[
        gsmtasks.components.schemas.location.Location, pydantic.Field()
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


TimeLocationFeature.update_forward_refs()

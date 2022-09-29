from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import lapidary_base.absent
import uuid
class SMS(pydantic.BaseModel):
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

    external_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=34,
        )
    ] = lapidary_base.absent.ABSENT

    state: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    notification: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    sender: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    alphanumeric_sender_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=20,
        )
    ] = lapidary_base.absent.ABSENT

    phone: typing.Annotated[
        str,
        pydantic.Field(
            max_length=128,
        )
    ]

    message: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    segments_count: typing.Annotated[
        typing.Union[
            int,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            gt=-2147483648.0,
            le=2147483647.0,
        )
    ] = lapidary_base.absent.ABSENT

    error: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    sent_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    failed_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    received_at: typing.Annotated[
        datetime.datetime,
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

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

SMS.update_forward_refs()

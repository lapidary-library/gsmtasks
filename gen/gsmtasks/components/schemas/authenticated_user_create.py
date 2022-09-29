from __future__ import annotations

import typing
import lapidary_base
import pydantic
import gsmtasks.components.schemas.nested_address
import lapidary_base.absent
import uuid


class AuthenticatedUserCreate(pydantic.BaseModel):
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

    first_name: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=30,
        ),
    ] = lapidary_base.absent.ABSENT

    last_name: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=30,
        ),
    ] = lapidary_base.absent.ABSENT

    display_name: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    email: typing.Annotated[str, pydantic.Field()]

    phone: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=128,
        ),
    ] = lapidary_base.absent.ABSENT

    password: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.write,
        ),
    ] = lapidary_base.absent.ABSENT

    address: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.nested_address.NestedAddress,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


AuthenticatedUserCreate.update_forward_refs()

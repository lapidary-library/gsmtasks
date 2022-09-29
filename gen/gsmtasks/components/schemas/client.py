from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import lapidary_base.absent
import uuid


class ClientContactAddressesItem(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


class Client(pydantic.BaseModel):
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

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=200,
        ),
    ]

    slug: typing.Annotated[
        str,
        pydantic.Field(
            regex=r"^[-a-zA-Z0-9_]+$",
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    archived: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
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

    contact_addresses: typing.Annotated[
        list[
            ClientContactAddressesItem,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


ClientContactAddressesItem.update_forward_refs()
Client.update_forward_refs()

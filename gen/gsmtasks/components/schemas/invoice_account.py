from __future__ import annotations

import typing
import lapidary_base
import pydantic
import lapidary_base.absent
import uuid


class InvoiceAccount(pydantic.BaseModel):
    id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    slug: typing.Annotated[
        str,
        pydantic.Field(
            regex=r"^[-a-zA-Z0-9_]+$",
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
        ),
    ]

    registry_code: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=20,
        ),
    ] = lapidary_base.absent.ABSENT

    vatin: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=20,
        ),
    ] = lapidary_base.absent.ABSENT

    billing_reference: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=20,
        ),
    ] = lapidary_base.absent.ABSENT

    billing_email: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=254,
        ),
    ] = lapidary_base.absent.ABSENT

    billing_vat: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


InvoiceAccount.update_forward_refs()

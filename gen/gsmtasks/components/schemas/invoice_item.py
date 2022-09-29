from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import lapidary_base.absent
import uuid
class InvoiceItem(pydantic.BaseModel):
    id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    invoice: typing.Annotated[
        str,
        pydantic.Field(
        )
    ]

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=200,
        )
    ]

    unit_price: typing.Annotated[
        str,
        pydantic.Field(
            regex=r'^-?\d{0,7}(?:\.\d{0,2})?$',
        )
    ]

    quantity: typing.Annotated[
        str,
        pydantic.Field(
            regex=r'^-?\d{0,7}(?:\.\d{0,4})?$',
        )
    ]

    unit: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=50,
        )
    ] = lapidary_base.absent.ABSENT

    total: typing.Annotated[
        str,
        pydantic.Field(
            regex=r'^-?\d{0,7}(?:\.\d{0,2})?$',
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

InvoiceItem.update_forward_refs()

from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.invoice_item
import lapidary_base.absent
import uuid
class Invoice(pydantic.BaseModel):
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
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    billing_method: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    state: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    period: typing.Annotated[
        list[
            datetime.date,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    total_no_vat: typing.Annotated[
        str,
        pydantic.Field(
            regex=r'^-?\d{0,7}(?:\.\d{0,2})?$',
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    total_vat: typing.Annotated[
        str,
        pydantic.Field(
            regex=r'^-?\d{0,7}(?:\.\d{0,2})?$',
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    total_with_vat: typing.Annotated[
        str,
        pydantic.Field(
            regex=r'^-?\d{0,7}(?:\.\d{0,2})?$',
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    currency: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    vat: typing.Annotated[
        bool,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    due_date: typing.Annotated[
        typing.Union[
            datetime.date,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    paid_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    items: typing.Annotated[
        list[
            gsmtasks.components.schemas.invoice_item.InvoiceItem,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    pricing: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    confirmed_by: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    confirmed_at: typing.Annotated[
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

    updated_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

Invoice.update_forward_refs()

from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import gsmtasks.components.schemas.null_enum
import gsmtasks.components.schemas.stripe_payment_state_enum
import gsmtasks.components.schemas.stripe_state_enum
import lapidary_base.absent
import uuid


class StripePayment(pydantic.BaseModel):
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

    billable_account: typing.Annotated[str, pydantic.Field()]

    invoice: typing.Annotated[
        typing.Union[
            str,
            None,
        ],
        pydantic.Field(),
    ]

    state: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.stripe_payment_state_enum.StripePaymentStateEnum,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    stripe_id: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=36,
        ),
    ] = lapidary_base.absent.ABSENT

    stripe_state: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.stripe_state_enum.StripeStateEnum,
            gsmtasks.components.schemas.null_enum.NullEnum,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    amount: typing.Annotated[
        str,
        pydantic.Field(
            regex=r"^-?\d{0,7}(?:\.\d{0,2})?$",
        ),
    ]

    currency: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=3,
        ),
    ] = lapidary_base.absent.ABSENT

    timestamp: typing.Annotated[
        typing.Union[
            datetime.datetime,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(),
    ] = lapidary_base.absent.ABSENT

    response: typing.Annotated[
        typing.Union[
            str,
            None,
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

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


StripePayment.update_forward_refs()

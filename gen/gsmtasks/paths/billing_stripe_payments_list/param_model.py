from __future__ import annotations

import typing
import lapidary_base
import pydantic
import enum
import lapidary_base.absent
class BillingStripePaymentsListFormat(enum.Enum):
    json = 'json'
    xlsx = 'xlsx'

class BillingStripePaymentsListState(enum.Enum):
    draft = 'draft'
    failed = 'failed'
    saved = 'saved'
    settled = 'settled'
    rejected = 'rejected'
    retried = 'retried'
    cancelled = 'cancelled'

class BillingStripePaymentsListStripeState(enum.Enum):
    none = None
    requires_payment_method = 'requires_payment_method'
    requires_confirmation = 'requires_confirmation'
    requires_capture = 'requires_capture'
    requires_action = 'requires_action'
    processing = 'processing'
    succeeded = 'succeeded'
    canceled = 'canceled'

class BillingStripePaymentsList(pydantic.BaseModel):
    q_billable_account: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='billable_account',
        )
    ] = lapidary_base.absent.ABSENT

    q_cursor: typing.Annotated[
        typing.Union[
            int,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='cursor',
        )
    ] = lapidary_base.absent.ABSENT

    q_format: typing.Annotated[
        typing.Union[
            BillingStripePaymentsListFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='format',
        )
    ] = lapidary_base.absent.ABSENT

    q_invoice: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='invoice',
        )
    ] = lapidary_base.absent.ABSENT

    q_ordering: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='ordering',
        )
    ] = lapidary_base.absent.ABSENT

    q_page_size: typing.Annotated[
        typing.Union[
            int,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='page_size',
        )
    ] = lapidary_base.absent.ABSENT

    q_state: typing.Annotated[
        typing.Union[
            BillingStripePaymentsListState,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='state',
        )
    ] = lapidary_base.absent.ABSENT

    q_stripe_state: typing.Annotated[
        typing.Union[
            BillingStripePaymentsListStripeState,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='stripe_state',
        )
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

BillingStripePaymentsList.update_forward_refs()

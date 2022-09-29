from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import enum
import lapidary_base.absent
class EmailsListFormat(enum.Enum):
    json = 'json'
    xlsx = 'xlsx'

class EmailsListState(enum.Enum):
    queued = 'queued'
    over_quota = 'over_quota'
    sent = 'sent'
    failed = 'failed'
    received = 'received'

class EmailsList(pydantic.BaseModel):
    q_account: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='account',
        )
    ] = lapidary_base.absent.ABSENT

    q_created_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='created_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_created_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='created_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_created_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='created_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_created_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='created_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_created_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='created_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_created_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='created_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_created_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='created_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_created_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='created_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_created_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='created_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_created_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='created_at__lte_or_isnull',
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

    q_external_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='external_id',
        )
    ] = lapidary_base.absent.ABSENT

    q_external_id__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='external_id__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_failed_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='failed_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_failed_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='failed_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_failed_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='failed_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_failed_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='failed_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_failed_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='failed_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_failed_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='failed_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_failed_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='failed_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_failed_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='failed_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_failed_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='failed_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_failed_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='failed_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_format: typing.Annotated[
        typing.Union[
            EmailsListFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='format',
        )
    ] = lapidary_base.absent.ABSENT

    q_from_email: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='from_email',
        )
    ] = lapidary_base.absent.ABSENT

    q_from_email__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='from_email__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='id',
        )
    ] = lapidary_base.absent.ABSENT

    q_message: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='message',
        )
    ] = lapidary_base.absent.ABSENT

    q_message__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='message__icontains',
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

    q_received_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='received_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_received_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='received_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_received_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='received_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_received_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='received_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_received_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='received_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_received_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='received_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_received_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='received_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_received_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='received_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_received_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='received_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_received_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='received_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_reply_to_email: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='reply_to_email',
        )
    ] = lapidary_base.absent.ABSENT

    q_reply_to_email__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='reply_to_email__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='search',
        )
    ] = lapidary_base.absent.ABSENT

    q_sent_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='sent_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_sent_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='sent_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_sent_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='sent_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_sent_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='sent_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_sent_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='sent_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_sent_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='sent_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_sent_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='sent_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_sent_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='sent_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_sent_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='sent_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_sent_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='sent_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_state: typing.Annotated[
        typing.Union[
            EmailsListState,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='state',
        )
    ] = lapidary_base.absent.ABSENT

    q_state__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='state__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_subject: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='subject',
        )
    ] = lapidary_base.absent.ABSENT

    q_subject__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='subject__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_updated_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='updated_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_updated_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='updated_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_updated_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='updated_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_updated_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='updated_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_updated_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='updated_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_updated_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='updated_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_updated_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='updated_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_updated_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='updated_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_updated_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='updated_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_updated_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='updated_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

EmailsList.update_forward_refs()

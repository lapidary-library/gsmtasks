from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import enum
import lapidary_base.absent
import uuid
class TaskExportsListAssigneeProximity(enum.Enum):
    away = 'away'
    near = 'near'

class TaskExportsListCategory(enum.Enum):
    assignment = 'assignment'
    pick_up = 'pick_up'
    drop_off = 'drop_off'
    warehouse = 'warehouse'

class TaskExportsListFormat(enum.Enum):
    json = 'json'
    xlsx = 'xlsx'

class TaskExportsListState(enum.Enum):
    unassigned = 'unassigned'
    assigned = 'assigned'
    accepted = 'accepted'
    transit = 'transit'
    active = 'active'
    completed = 'completed'
    failed = 'failed'
    cancelled = 'cancelled'

class TaskExportsList(pydantic.BaseModel):
    q_account: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='account',
        )
    ] = lapidary_base.absent.ABSENT

    q_account__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='account__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__apartment_number: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__apartment_number',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__apartment_number__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__apartment_number__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__apartment_number__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__apartment_number__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__apartment_number__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__apartment_number__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__apartment_number__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__apartment_number__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__apartment_number__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__apartment_number__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__city: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__city',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__city__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__city__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__city__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__city__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__city__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__city__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__city__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__city__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__city__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__city__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__country: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__country__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__country__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__country__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__country__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__country__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__country_code: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country_code',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__country_code__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country_code__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__country_code__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country_code__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__country_code__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country_code__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__country_code__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country_code__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__country_code__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country_code__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__formatted_address: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__formatted_address',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__formatted_address__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__formatted_address__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__formatted_address__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__formatted_address__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__formatted_address__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__formatted_address__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__formatted_address__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__formatted_address__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__formatted_address__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__formatted_address__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocode_failed_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocode_failed_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocode_failed_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocode_failed_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocode_failed_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocode_failed_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocode_failed_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocode_failed_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocode_failed_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocode_failed_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocode_failed_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocode_failed_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocode_failed_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocode_failed_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocode_failed_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocode_failed_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocode_failed_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocode_failed_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocode_failed_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocode_failed_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocoded_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocoded_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocoded_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocoded_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocoded_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocoded_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocoded_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocoded_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocoded_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocoded_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocoded_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocoded_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocoded_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocoded_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocoded_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocoded_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocoded_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocoded_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__geocoded_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__geocoded_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__google_place_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__google_place_id',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__google_place_id__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__google_place_id__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__google_place_id__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__google_place_id__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__google_place_id__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__google_place_id__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__google_place_id__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__google_place_id__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__google_place_id__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__google_place_id__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__house_number: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__house_number',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__house_number__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__house_number__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__house_number__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__house_number__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__house_number__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__house_number__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__house_number__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__house_number__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__house_number__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__house_number__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__point_of_interest: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__point_of_interest',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__point_of_interest__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__point_of_interest__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__point_of_interest__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__point_of_interest__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__point_of_interest__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__point_of_interest__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__point_of_interest__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__point_of_interest__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__point_of_interest__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__point_of_interest__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__postal_code: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__postal_code',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__postal_code__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__postal_code__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__postal_code__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__postal_code__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__postal_code__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__postal_code__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__postal_code__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__postal_code__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__postal_code__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__postal_code__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__raw_address: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__raw_address',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__raw_address__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__raw_address__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__raw_address__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__raw_address__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__raw_address__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__raw_address__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__raw_address__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__raw_address__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__raw_address__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__raw_address__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__state: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__state',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__state__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__state__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__state__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__state__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__state__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__state__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__state__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__state__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__state__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__state__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__street: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__street',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__street__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__street__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__street__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__street__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__street__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__street__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__street__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__street__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_address__street__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__street__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_address_data: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address_data',
        )
    ] = lapidary_base.absent.ABSENT

    q_address_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address_id',
        )
    ] = lapidary_base.absent.ABSENT

    q_address_id__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address_id__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_address_id__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address_id__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__email: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__email',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__email__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__email__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__email__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__email__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__email__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__email__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__email__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__email__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__email__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__email__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__first_name: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__first_name',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__first_name__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__first_name__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__first_name__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__first_name__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__first_name__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__first_name__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__first_name__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__first_name__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__first_name__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__first_name__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__last_name: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__last_name',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__last_name__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__last_name__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__last_name__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__last_name__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__last_name__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__last_name__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__last_name__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__last_name__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__last_name__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__last_name__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__phone: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__phone',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__phone__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__phone__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__phone__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__phone__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__phone__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__phone__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__phone__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__phone__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee__phone__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee__phone__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee_id',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee_id__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee_id__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee_id__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee_id__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee_proximity: typing.Annotated[
        typing.Union[
            TaskExportsListAssigneeProximity,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee_proximity',
        )
    ] = lapidary_base.absent.ABSENT

    q_assignee_proximity__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='assignee_proximity__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_barcodes__contained_by: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='barcodes__contained_by',
        )
    ] = lapidary_base.absent.ABSENT

    q_barcodes__contains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='barcodes__contains',
        )
    ] = lapidary_base.absent.ABSENT

    q_barcodes__isnull: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='barcodes__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_barcodes__overlap: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='barcodes__overlap',
        )
    ] = lapidary_base.absent.ABSENT

    q_cancelled_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='cancelled_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_cancelled_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='cancelled_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_cancelled_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='cancelled_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_cancelled_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='cancelled_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_cancelled_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='cancelled_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_cancelled_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='cancelled_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_cancelled_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='cancelled_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_cancelled_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='cancelled_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_cancelled_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='cancelled_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_cancelled_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='cancelled_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_category: typing.Annotated[
        typing.Union[
            TaskExportsListCategory,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='category',
        )
    ] = lapidary_base.absent.ABSENT

    q_category__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='category__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_after__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_after__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_after__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_after__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_after__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_after__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_after__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_after__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_after__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_after__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_after__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_after__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_after__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_after__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_after__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_after__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_after__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_after__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_after__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_after__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_before__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_before__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_before__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_before__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_before__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_before__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_before__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_before__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_before__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_before__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_before__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_before__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_before__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_before__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_before__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_before__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_before__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_before__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_complete_before__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='complete_before__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_completed_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='completed_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_completed_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='completed_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_completed_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='completed_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_completed_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='completed_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_completed_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='completed_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_completed_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='completed_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_completed_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='completed_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_completed_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='completed_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_completed_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='completed_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_completed_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='completed_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__company__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__company__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__company__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__company__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__company__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__company__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__company__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__company__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__company__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__company__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__email: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__email',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__email__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__email__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__email__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__email__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__email__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__email__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__email__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__email__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__email__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__email__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__name: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__name',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__name__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__name__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__name__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__name__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__name__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__name__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__name__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__name__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__name__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__name__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__notes: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__notes',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__notes__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__notes__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__notes__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__notes__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__notes__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__notes__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__notes__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__notes__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__notes__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__notes__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phone: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phone',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phone__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phone__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phone__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phone__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phone__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phone__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phone__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phone__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phone__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phone__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact_data: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact_data',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact_id',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact_id__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact_id__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact_id__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact_id__isnull',
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

    q_created_by: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='created_by',
        )
    ] = lapidary_base.absent.ABSENT

    q_created_by__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='created_by__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_created_by__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='created_by__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_description: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='description',
        )
    ] = lapidary_base.absent.ABSENT

    q_description__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='description__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_description__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='description__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_description__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='description__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_description__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='description__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_duration: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='duration',
        )
    ] = lapidary_base.absent.ABSENT

    q_duration__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='duration__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_duration__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='duration__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_duration__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='duration__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_duration__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='duration__lte',
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

    q_external_id__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='external_id__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_external_id__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='external_id__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_external_id__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='external_id__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_external_id__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='external_id__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_external_id__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='external_id__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_fields: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='fields',
        )
    ] = lapidary_base.absent.ABSENT

    q_format: typing.Annotated[
        typing.Union[
            TaskExportsListFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='format',
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

    q_id__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='id__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_is_optimal: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='is_optimal',
        )
    ] = lapidary_base.absent.ABSENT

    q_is_optimal__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='is_optimal__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__accepted_distance: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__accepted_distance',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__accepted_distance__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__accepted_distance__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__accepted_distance__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__accepted_distance__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__accepted_distance__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__accepted_distance__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__accepted_distance__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__accepted_distance__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__accepted_duration: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__accepted_duration',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__accepted_duration__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__accepted_duration__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__accepted_duration__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__accepted_duration__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__accepted_duration__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__accepted_duration__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__accepted_duration__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__accepted_duration__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__active_distance: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__active_distance',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__active_distance__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__active_distance__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__active_distance__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__active_distance__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__active_distance__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__active_distance__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__active_distance__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__active_distance__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__active_duration: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__active_duration',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__active_duration__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__active_duration__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__active_duration__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__active_duration__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__active_duration__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__active_duration__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__active_duration__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__active_duration__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__assigned_distance: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__assigned_distance',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__assigned_distance__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__assigned_distance__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__assigned_distance__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__assigned_distance__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__assigned_distance__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__assigned_distance__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__assigned_distance__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__assigned_distance__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__assigned_duration: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__assigned_duration',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__assigned_duration__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__assigned_duration__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__assigned_duration__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__assigned_duration__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__assigned_duration__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__assigned_duration__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__assigned_duration__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__assigned_duration__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__cancelled_distance: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__cancelled_distance',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__cancelled_distance__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__cancelled_distance__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__cancelled_distance__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__cancelled_distance__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__cancelled_distance__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__cancelled_distance__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__cancelled_distance__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__cancelled_distance__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__cancelled_duration: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__cancelled_duration',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__cancelled_duration__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__cancelled_duration__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__cancelled_duration__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__cancelled_duration__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__cancelled_duration__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__cancelled_duration__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__cancelled_duration__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__cancelled_duration__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__completed_distance: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__completed_distance',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__completed_distance__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__completed_distance__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__completed_distance__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__completed_distance__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__completed_distance__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__completed_distance__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__completed_distance__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__completed_distance__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__completed_duration: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__completed_duration',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__completed_duration__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__completed_duration__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__completed_duration__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__completed_duration__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__completed_duration__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__completed_duration__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__completed_duration__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__completed_duration__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__documents_count: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__documents_count',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__documents_count__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__documents_count__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__documents_count__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__documents_count__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__documents_count__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__documents_count__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__documents_count__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__documents_count__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__events_count: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__events_count',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__events_count__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__events_count__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__events_count__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__events_count__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__events_count__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__events_count__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__events_count__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__events_count__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__failed_distance: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__failed_distance',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__failed_distance__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__failed_distance__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__failed_distance__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__failed_distance__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__failed_distance__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__failed_distance__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__failed_distance__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__failed_distance__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__failed_duration: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__failed_duration',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__failed_duration__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__failed_duration__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__failed_duration__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__failed_duration__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__failed_duration__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__failed_duration__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__failed_duration__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__failed_duration__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__forms_completed_count: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__forms_completed_count',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__forms_completed_count__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__forms_completed_count__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__forms_completed_count__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__forms_completed_count__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__forms_completed_count__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__forms_completed_count__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__forms_completed_count__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__forms_completed_count__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__forms_count: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__forms_count',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__forms_count__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__forms_count__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__forms_count__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__forms_count__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__forms_count__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__forms_count__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__forms_count__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__forms_count__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_accepted_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_accepted_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_accepted_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_accepted_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_accepted_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_accepted_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_accepted_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_accepted_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_accepted_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_accepted_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_accepted_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_accepted_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_accepted_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_accepted_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_accepted_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_accepted_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_accepted_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_accepted_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_accepted_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_accepted_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_active_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_active_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_active_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_active_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_active_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_active_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_active_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_active_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_active_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_active_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_active_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_active_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_active_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_active_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_active_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_active_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_active_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_active_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_active_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_active_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_assigned_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_assigned_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_assigned_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_assigned_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_assigned_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_assigned_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_assigned_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_assigned_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_assigned_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_assigned_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_assigned_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_assigned_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_assigned_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_assigned_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_assigned_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_assigned_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_assigned_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_assigned_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_assigned_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_assigned_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_cancelled_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_cancelled_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_cancelled_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_cancelled_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_cancelled_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_cancelled_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_cancelled_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_cancelled_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_cancelled_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_cancelled_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_cancelled_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_cancelled_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_cancelled_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_cancelled_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_cancelled_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_cancelled_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_cancelled_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_cancelled_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_cancelled_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_cancelled_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_completed_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_completed_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_completed_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_completed_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_completed_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_completed_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_completed_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_completed_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_completed_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_completed_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_completed_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_completed_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_completed_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_completed_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_completed_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_completed_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_completed_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_completed_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_completed_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_completed_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_failed_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_failed_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_failed_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_failed_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_failed_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_failed_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_failed_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_failed_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_failed_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_failed_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_failed_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_failed_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_failed_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_failed_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_failed_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_failed_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_failed_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_failed_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_failed_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_failed_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_transit_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_transit_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_transit_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_transit_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_transit_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_transit_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_transit_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_transit_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_transit_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_transit_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_transit_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_transit_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_transit_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_transit_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_transit_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_transit_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_transit_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_transit_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_transit_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_transit_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_unassigned_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_unassigned_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_unassigned_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_unassigned_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_unassigned_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_unassigned_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_unassigned_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_unassigned_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_unassigned_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_unassigned_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_unassigned_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_unassigned_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_unassigned_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_unassigned_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_unassigned_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_unassigned_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_unassigned_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_unassigned_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__last_unassigned_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__last_unassigned_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__signatures_count: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__signatures_count',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__signatures_count__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__signatures_count__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__signatures_count__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__signatures_count__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__signatures_count__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__signatures_count__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__signatures_count__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__signatures_count__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__task_event_notes_count: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__task_event_notes_count',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__task_event_notes_count__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__task_event_notes_count__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__task_event_notes_count__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__task_event_notes_count__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__task_event_notes_count__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__task_event_notes_count__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__task_event_notes_count__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__task_event_notes_count__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__transit_distance: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__transit_distance',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__transit_distance__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__transit_distance__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__transit_distance__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__transit_distance__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__transit_distance__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__transit_distance__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__transit_distance__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__transit_distance__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__transit_duration: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__transit_duration',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__transit_duration__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__transit_duration__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__transit_duration__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__transit_duration__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__transit_duration__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__transit_duration__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__transit_duration__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__transit_duration__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__unassigned_distance: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__unassigned_distance',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__unassigned_distance__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__unassigned_distance__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__unassigned_distance__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__unassigned_distance__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__unassigned_distance__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__unassigned_distance__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__unassigned_distance__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__unassigned_distance__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__unassigned_duration: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__unassigned_duration',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__unassigned_duration__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__unassigned_duration__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__unassigned_duration__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__unassigned_duration__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__unassigned_duration__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__unassigned_duration__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_metadata__unassigned_duration__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metadata__unassigned_duration__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_metafields__namespace_key: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='metafields__namespace:key',
        )
    ] = lapidary_base.absent.ABSENT

    q_order: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__auto_assign: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__auto_assign',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__created_at__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__created_at__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__created_at__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__created_at__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__created_at__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__created_at__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__created_at__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__created_at__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__created_at__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__created_at__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__created_at__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__created_at__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__created_at__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__created_at__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__created_at__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__created_at__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__created_at__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__created_at__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__created_at__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__created_at__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__created_by: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__created_by',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__created_by__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__created_by__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__created_by__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__created_by__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__external_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__external_id',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__external_id__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__external_id__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__external_id__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__external_id__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__external_id__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__external_id__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__external_id__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__external_id__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__external_id__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__external_id__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__external_id__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__external_id__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__reference: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__reference',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__reference__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__reference__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__reference__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__reference__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__reference__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__reference__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__reference__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__reference__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_order__reference__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order__reference__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_order_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order_id',
        )
    ] = lapidary_base.absent.ABSENT

    q_order_id__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order_id__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_order_id__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='order_id__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_orderer: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='orderer',
        )
    ] = lapidary_base.absent.ABSENT

    q_orderer__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='orderer__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_orderer_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='orderer_id',
        )
    ] = lapidary_base.absent.ABSENT

    q_orderer_id__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='orderer_id__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_orderer_id__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='orderer_id__isnull',
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

    q_owner_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='owner_id',
        )
    ] = lapidary_base.absent.ABSENT

    q_owner_id__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='owner_id__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_owner_id__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='owner_id__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_page: typing.Annotated[
        typing.Union[
            int,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='page',
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

    q_position__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='position__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_position__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='position__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_position__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='position__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_position__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='position__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_position__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='position__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_position__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='position__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_position__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='position__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_position__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='position__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_position__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='position__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_position__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='position__lte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_previous_assignees__contained_by: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='previous_assignees__contained_by',
        )
    ] = lapidary_base.absent.ABSENT

    q_previous_assignees__contains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='previous_assignees__contains',
        )
    ] = lapidary_base.absent.ABSENT

    q_previous_assignees__isnull: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='previous_assignees__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_previous_assignees__overlap: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='previous_assignees__overlap',
        )
    ] = lapidary_base.absent.ABSENT

    q_priority: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='priority',
        )
    ] = lapidary_base.absent.ABSENT

    q_priority__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='priority__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_priority__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='priority__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_priority__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='priority__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_priority__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='priority__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_priority__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='priority__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_receiver: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='receiver',
        )
    ] = lapidary_base.absent.ABSENT

    q_receiver__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='receiver__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_receiver_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='receiver_id',
        )
    ] = lapidary_base.absent.ABSENT

    q_receiver_id__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='receiver_id__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_receiver_id__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='receiver_id__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_reference: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='reference',
        )
    ] = lapidary_base.absent.ABSENT

    q_reference__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='reference__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_reference__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='reference__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_reference__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='reference__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_reference__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='reference__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_reference__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='reference__search',
        )
    ] = lapidary_base.absent.ABSENT

    q_route: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='route',
        )
    ] = lapidary_base.absent.ABSENT

    q_route__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='route__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_route_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='route_id',
        )
    ] = lapidary_base.absent.ABSENT

    q_route_id__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='route_id__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_route_id__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='route_id__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_scheduled_time__date: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='scheduled_time__date',
        )
    ] = lapidary_base.absent.ABSENT

    q_scheduled_time__date_or_isnull: typing.Annotated[
        typing.Union[
            datetime.date,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='scheduled_time__date_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_scheduled_time__gt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='scheduled_time__gt',
        )
    ] = lapidary_base.absent.ABSENT

    q_scheduled_time__gt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='scheduled_time__gt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_scheduled_time__gte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='scheduled_time__gte',
        )
    ] = lapidary_base.absent.ABSENT

    q_scheduled_time__gte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='scheduled_time__gte_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_scheduled_time__lt: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='scheduled_time__lt',
        )
    ] = lapidary_base.absent.ABSENT

    q_scheduled_time__lt_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='scheduled_time__lt_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_scheduled_time__lte: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='scheduled_time__lte',
        )
    ] = lapidary_base.absent.ABSENT

    q_scheduled_time__lte_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='scheduled_time__lte_or_isnull',
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

    q_size__contained_by: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='size__contained_by',
        )
    ] = lapidary_base.absent.ABSENT

    q_size__contains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='size__contains',
        )
    ] = lapidary_base.absent.ABSENT

    q_size__isnull: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='size__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_size__overlap: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='size__overlap',
        )
    ] = lapidary_base.absent.ABSENT

    q_state: typing.Annotated[
        typing.Union[
            TaskExportsListState,
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

    q_state__in_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='state__in_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_state__not_in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='state__not_in',
        )
    ] = lapidary_base.absent.ABSENT

    q_state__not_in_or_isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='state__not_in_or_isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_task_import: typing.Annotated[
        typing.Union[
            uuid.UUID,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='task_import',
        )
    ] = lapidary_base.absent.ABSENT

    q_task_import__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='task_import__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_unassignee_id: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='unassignee_id',
        )
    ] = lapidary_base.absent.ABSENT

    q_unassignee_id__in: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='unassignee_id__in',
        )
    ] = lapidary_base.absent.ABSENT

    q_unassignee_id__isnull: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='unassignee_id__isnull',
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

TaskExportsList.update_forward_refs()

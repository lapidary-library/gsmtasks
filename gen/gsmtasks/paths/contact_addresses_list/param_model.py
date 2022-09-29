from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import enum
import lapidary_base.absent
class ContactAddressesListFormat(enum.Enum):
    json = 'json'
    xlsx = 'xlsx'

class ContactAddressesList(pydantic.BaseModel):
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

    q_address__apartment_number__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__apartment_number__iexact',
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

    q_address__city__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__city__iexact',
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

    q_address__country__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country__iexact',
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

    q_address__country_code__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__country_code__iexact',
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

    q_address__formatted_address__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__formatted_address__iexact',
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

    q_address__postal_code__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__postal_code__iexact',
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

    q_address__state__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__state__iexact',
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

    q_address__street__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='address__street__iexact',
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

    q_client: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='client',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__company: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__company',
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

    q_contact__company__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__company__iexact',
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

    q_contact__emails__contained_by: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__emails__contained_by',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__emails__contains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__emails__contains',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__emails__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__emails__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__emails__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__emails__iexact',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__emails__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__emails__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__emails__isnull: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__emails__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__emails__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__emails__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__emails__overlap: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__emails__overlap',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__emails__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__emails__search',
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

    q_contact__name__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__name__iexact',
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

    q_contact__notes__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__notes__iexact',
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

    q_contact__phones__contained_by: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phones__contained_by',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phones__contains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phones__contains',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phones__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phones__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phones__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phones__iexact',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phones__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phones__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phones__isnull: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phones__isnull',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phones__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phones__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phones__overlap: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phones__overlap',
        )
    ] = lapidary_base.absent.ABSENT

    q_contact__phones__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='contact__phones__search',
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

    q_format: typing.Annotated[
        typing.Union[
            ContactAddressesListFormat,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='format',
        )
    ] = lapidary_base.absent.ABSENT

    q_is_orderer: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='is_orderer',
        )
    ] = lapidary_base.absent.ABSENT

    q_is_receiver: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='is_receiver',
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

    q_source: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='source',
        )
    ] = lapidary_base.absent.ABSENT

    q_source__icontains: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='source__icontains',
        )
    ] = lapidary_base.absent.ABSENT

    q_source__iexact: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='source__iexact',
        )
    ] = lapidary_base.absent.ABSENT

    q_source__iregex: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='source__iregex',
        )
    ] = lapidary_base.absent.ABSENT

    q_source__istartswith: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='source__istartswith',
        )
    ] = lapidary_base.absent.ABSENT

    q_source__search: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.query,
            alias='source__search',
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

ContactAddressesList.update_forward_refs()

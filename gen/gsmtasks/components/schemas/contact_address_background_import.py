from __future__ import annotations

import typing
import lapidary_base
import pydantic
import datetime
import uuid
class ContactAddressBackgroundImportContactAddressesDataItem(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class ContactAddressBackgroundImportErrors(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class ContactAddressBackgroundImport(pydantic.BaseModel):
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
        str,
        pydantic.Field(
        )
    ]

    created_by: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    contact_addresses_data: typing.Annotated[
        list[
            ContactAddressBackgroundImportContactAddressesDataItem,
        ],
        pydantic.Field(
            direction=lapidary_base.ParamDirection.write,
        )
    ]

    state: typing.Annotated[
        typing.Any,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    started_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    completed_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    failed_at: typing.Annotated[
        datetime.datetime,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    errors: typing.Annotated[
        ContactAddressBackgroundImportErrors,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    celery_task_id: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    contact_addresses_created: typing.Annotated[
        list[
            str,
        ],
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

ContactAddressBackgroundImportContactAddressesDataItem.update_forward_refs()
ContactAddressBackgroundImportErrors.update_forward_refs()
ContactAddressBackgroundImport.update_forward_refs()

from __future__ import annotations

import typing
import lapidary_base
import pydantic
import gsmtasks.components.schemas.blank_enum
import gsmtasks.components.schemas.country_code_enum
import gsmtasks.components.schemas.null_enum
import gsmtasks.components.schemas.timezone_enum
import gsmtasks.components.schemas.type21d_enum
import lapidary_base.absent
import uuid
class RegistrationAccount(pydantic.BaseModel):
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

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=100,
        )
    ]

    type: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.type21d_enum.Type21dEnum,
            gsmtasks.components.schemas.blank_enum.BlankEnum,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    language: typing.Annotated[
        typing.Union[
            typing.Any,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    timezone: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.timezone_enum.TimezoneEnum,
            gsmtasks.components.schemas.blank_enum.BlankEnum,
            gsmtasks.components.schemas.null_enum.NullEnum,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    country_code: typing.Annotated[
        typing.Union[
            gsmtasks.components.schemas.country_code_enum.CountryCodeEnum,
            gsmtasks.components.schemas.blank_enum.BlankEnum,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    website: typing.Annotated[
        typing.Union[
            str,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=200,
        )
    ] = lapidary_base.absent.ABSENT

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

RegistrationAccount.update_forward_refs()

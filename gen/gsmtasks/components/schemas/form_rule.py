from __future__ import annotations

import typing
import lapidary_base
import pydantic
import lapidary_base.absent
import uuid
class FormRuleRules(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

class FormRule(pydantic.BaseModel):
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

    is_active: typing.Annotated[
        typing.Union[
            bool,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
        )
    ] = lapidary_base.absent.ABSENT

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=50,
        )
    ]

    edit_url: typing.Annotated[
        str,
        pydantic.Field(
            max_length=200,
        )
    ]

    view_url: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=200,
        )
    ] = lapidary_base.absent.ABSENT

    pdf_url: typing.Annotated[
        typing.Union[
            str,
            None,
            lapidary_base.absent.Absent,
        ],
        pydantic.Field(
            max_length=200,
        )
    ] = lapidary_base.absent.ABSENT

    rules: typing.Annotated[
        FormRuleRules,
        pydantic.Field(
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

FormRuleRules.update_forward_refs()
FormRule.update_forward_refs()

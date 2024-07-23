# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import gsmtasks.components.schemas.FormRule.properties.rules.schema


class FormRule(lapidary.runtime.ModelBase):
    account: str

    name: typing.Annotated[
        str,
        pydantic.Field(
            max_length=50,
        )
    ]

    edit_url: typing.Annotated[
        str,
        pydantic.Field(
            max_length=2048,
        )
    ]

    rules: gsmtasks.components.schemas.FormRule.properties.rules.schema.rules

    id: typing.Union[None, str] = None

    url: typing.Union[None, str] = None

    is_active: typing.Union[None, bool] = None

    view_url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=2048,
        )
    ] = None

    pdf_url: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=2048,
        )
    ] = None

    open_in: typing.Union[None, str] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

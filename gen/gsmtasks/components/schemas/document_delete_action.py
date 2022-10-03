from __future__ import annotations

import typing
import lapidary_base
import pydantic


class DocumentDeleteAction(pydantic.BaseModel):
    account: typing.Annotated[str, pydantic.Field()]

    documents: typing.Annotated[
        list[
            str,
        ],
        pydantic.Field(),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


DocumentDeleteAction.update_forward_refs()
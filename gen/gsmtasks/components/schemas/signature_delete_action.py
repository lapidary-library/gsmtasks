from __future__ import annotations

import typing
import lapidary_base
import pydantic


class SignatureDeleteAction(pydantic.BaseModel):
    account: typing.Annotated[str, pydantic.Field()]

    signatures: typing.Annotated[
        list[
            str,
        ],
        pydantic.Field(),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


SignatureDeleteAction.update_forward_refs()

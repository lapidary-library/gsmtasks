from __future__ import annotations

import typing
import lapidary_base
import pydantic
import uuid


class AccountRoleToken(pydantic.BaseModel):
    token: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


AccountRoleToken.update_forward_refs()

from __future__ import annotations

import typing
import lapidary_base
import pydantic
import uuid


class AccountRoleActivation(pydantic.BaseModel):
    token: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.write,
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


AccountRoleActivation.update_forward_refs()

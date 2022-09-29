from __future__ import annotations

import typing
import lapidary_base
import pydantic
import gsmtasks.components.schemas.registration_account
import gsmtasks.components.schemas.registration_user
class Registration(pydantic.BaseModel):
    account: typing.Annotated[
        gsmtasks.components.schemas.registration_account.RegistrationAccount,
        pydantic.Field(
        )
    ]

    user: typing.Annotated[
        gsmtasks.components.schemas.registration_user.RegistrationUser,
        pydantic.Field(
        )
    ]

    token: typing.Annotated[
        str,
        pydantic.Field(
            direction=lapidary_base.ParamDirection.read,
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

Registration.update_forward_refs()

from __future__ import annotations

import typing
import lapidary_base
import pydantic


class AccountOwnerChange(pydantic.BaseModel):
    owner: typing.Annotated[str, pydantic.Field()]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


AccountOwnerChange.update_forward_refs()

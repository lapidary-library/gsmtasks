from __future__ import annotations

import typing
import lapidary_base
import pydantic


class TaskAccountChange(pydantic.BaseModel):
    account: typing.Annotated[str, pydantic.Field()]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


TaskAccountChange.update_forward_refs()

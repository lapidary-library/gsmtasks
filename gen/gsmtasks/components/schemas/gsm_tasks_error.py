from __future__ import annotations

import typing
import lapidary_base
import pydantic
@pydantic.dataclasses.dataclass
class GSMTasksError(Exception):
    detail: str = pydantic.dataclasses.Field(
    )

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


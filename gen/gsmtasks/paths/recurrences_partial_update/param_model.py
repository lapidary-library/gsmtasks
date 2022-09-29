from __future__ import annotations

import typing
import lapidary_base
import pydantic
import uuid


class RecurrencesPartialUpdate(pydantic.BaseModel):
    p_id: typing.Annotated[
        uuid.UUID,
        pydantic.Field(
            in_=lapidary_base.ParamPlacement.path,
            alias="id",
        ),
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True


RecurrencesPartialUpdate.update_forward_refs()

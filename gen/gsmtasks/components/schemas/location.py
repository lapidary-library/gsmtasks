from __future__ import annotations

import typing
import lapidary_base
import pydantic
import gsmtasks.components.schemas.location_type_enum
class Location(pydantic.BaseModel):
    type: typing.Annotated[
        gsmtasks.components.schemas.location_type_enum.LocationTypeEnum,
        pydantic.Field(
        )
    ]

    coordinates: typing.Annotated[
        list[
            float,
        ],
        pydantic.Field(
            min_items=2,
            max_items=2,
        )
    ]

    class Config(pydantic.BaseConfig):
        allow_population_by_field_name = True

Location.update_forward_refs()

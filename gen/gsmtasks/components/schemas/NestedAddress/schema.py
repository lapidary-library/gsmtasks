# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import gsmtasks.components.schemas.Location.schema


class NestedAddress(lapidary.runtime.ModelBase):
    raw_address: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=250,
        )
    ] = None

    formatted_address: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=250,
        )
    ] = None

    location: typing.Union[None, gsmtasks.components.schemas.Location.schema.Location] = None

    google_place_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=250,
        )
    ] = None

    point_of_interest: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    street: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=200,
        )
    ] = None

    house_number: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    apartment_number: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    city: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    state: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    postal_code: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    country: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    country_code: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=2,
        )
    ] = None

    geocoded_at: typing.Union[None, datetime.datetime] = None

    geocode_failed_at: typing.Union[None, datetime.datetime] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

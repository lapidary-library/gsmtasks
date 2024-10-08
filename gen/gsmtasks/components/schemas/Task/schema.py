# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import datetime
import gsmtasks.components.schemas.Metafields.schema
import gsmtasks.components.schemas.NestedAddress.schema
import gsmtasks.components.schemas.NestedContact.schema
import gsmtasks.components.schemas.Task.properties.actions.schema
import gsmtasks.components.schemas.Task.properties.counts.schema
import gsmtasks.components.schemas.Task.properties.duration.schema
import gsmtasks.components.schemas.Task.properties.forms.schema
import uuid


class Task(lapidary.runtime.ModelBase):
    account: str

    address: gsmtasks.components.schemas.NestedAddress.schema.NestedAddress

    id: typing.Union[None, uuid.UUID] = None

    url: typing.Union[None, str] = None

    order: typing.Union[None, str] = None

    route: typing.Union[None, str] = None

    order_reference: typing.Union[None, str] = None

    external_id: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    category: typing.Union[None, str] = None

    orderer: typing.Union[None, str] = None

    orderer_name: typing.Union[None, str] = None

    receiver: typing.Union[None, str] = None

    contact: typing.Union[None, gsmtasks.components.schemas.NestedContact.schema.NestedContact] = None

    description: typing.Union[None, str] = None

    reference: typing.Annotated[
        typing.Union[None, str],
        pydantic.Field(
            max_length=100,
        )
    ] = None

    complete_after: typing.Union[None, datetime.datetime] = None

    complete_before: typing.Union[None, datetime.datetime] = None

    scheduled_time: typing.Union[None, datetime.datetime] = None

    state: typing.Union[None, str] = None

    completed_at: typing.Union[None, datetime.datetime] = None

    cancelled_at: typing.Union[None, datetime.datetime] = None

    assignee: typing.Union[None, str] = None

    auto_assign: typing.Union[None, bool] = None

    assignee_proximity: typing.Union[None, str] = None

    position: typing.Annotated[
        typing.Union[None, float],
        pydantic.Field(
            ge=0.0,
            le=253402300799.0,
        )
    ] = None

    priority: typing.Annotated[
        typing.Union[None, int],
        pydantic.Field(
            ge=-2147483648,
            le=2147483647,
        )
    ] = None

    duration: typing.Union[None, gsmtasks.components.schemas.Task.properties.duration.schema.duration] = None

    size: typing.Union[None, list[int]] = None

    is_full_load: typing.Union[None, bool] = None

    metafields: typing.Union[None, gsmtasks.components.schemas.Metafields.schema.Metafields] = None

    forms: typing.Union[None, gsmtasks.components.schemas.Task.properties.forms.schema.forms] = None

    created_by: typing.Union[None, str] = None

    issues: typing.Union[None, list[typing.Union[None, str]]] = None

    created_at: typing.Union[None, datetime.datetime] = None

    updated_at: typing.Union[None, datetime.datetime] = None

    events: typing.Union[None, str] = None

    documents: typing.Union[None, str] = None

    signatures: typing.Union[None, str] = None

    actions: typing.Union[None, gsmtasks.components.schemas.Task.properties.actions.schema.actions] = None

    counts: typing.Union[None, gsmtasks.components.schemas.Task.properties.counts.schema.counts] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

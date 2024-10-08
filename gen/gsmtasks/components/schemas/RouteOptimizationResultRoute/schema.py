# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing
import gsmtasks.components.schemas.RouteOptimizationResultTask.schema


class RouteOptimizationResultRoute(lapidary.runtime.ModelBase):
    assignee: str

    distance: int

    completion_time: int

    service_time: int

    transport_time: int

    waiting_time: int

    tasks: list[gsmtasks.components.schemas.RouteOptimizationResultTask.schema.RouteOptimizationResultTask]

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

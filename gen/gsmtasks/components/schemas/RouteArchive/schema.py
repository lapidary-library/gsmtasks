# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing


class RouteArchive(lapidary.runtime.ModelBase):
    task_action: typing.Union[None, str] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

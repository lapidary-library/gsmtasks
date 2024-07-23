# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing


class RenderResponse(lapidary.runtime.ModelBase):
    task: str

    sender: typing.Union[None, str] = None

    user: typing.Union[None, str] = None

    event: typing.Union[None, str, typing.Any] = None

    recipient: typing.Union[None, str, typing.Any] = None

    emails: typing.Union[None, list[str]] = None

    phones: typing.Union[None, list[str]] = None

    app: typing.Union[None, bool] = None

    message: typing.Union[None, str] = None

    model_config = pydantic.ConfigDict(
        extra='allow'
    )
# This file is automatically @generated by Lapidary and should not be changed by hand.

from __future__ import annotations

import lapidary.runtime
import pydantic
import typing_extensions as typing


class PasswordReset(lapidary.runtime.ModelBase):
    email: str

    model_config = pydantic.ConfigDict(
        extra='allow'
    )

from __future__ import annotations

import typing
import lapidary_base
import pydantic
import enum


class DateFormatEnum(enum.Enum):
    DD_MM_YYYY = "DD.MM.YYYY"
    YYYY_MM_DD = "YYYY-MM-DD"
    DD_MM_YYYY_ = "DD/MM/YYYY"
    MM_DD_YYYY = "MM/DD/YYYY"

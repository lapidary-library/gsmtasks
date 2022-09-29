from __future__ import annotations

import typing
import lapidary_base
import pydantic
import enum


class VersionEnum(enum.Enum):
    v_2_4_11 = "2.4.11"
    v_2_4_10 = "2.4.10"
    v_2_4_9 = "2.4.9"
    v_2_4_8 = "2.4.8"
    v_2_4_7 = "2.4.7"
    v_2_4_6 = "2.4.6"
    v_2_4_5 = "2.4.5"
    v_2_4_4 = "2.4.4"
    v_2_4_3 = "2.4.3"
    v_2_4_2 = "2.4.2"
    v_2_4_1 = "2.4.1"
    v_2_3_5 = "2.3.5"
    v_2_3_4 = "2.3.4"
    v_2_3_3 = "2.3.3"
    v_2_3_2 = "2.3.2"
    v_2_3_1 = "2.3.1"
    v_2_3_0 = "2.3.0"
    v_2_2_6 = "2.2.6"
    v_2_2_5 = "2.2.5"
    v_2_2_4 = "2.2.4"
    v_2_2_3 = "2.2.3"
    v_2_2_2 = "2.2.2"
    v_2_2_1 = "2.2.1"
    v_2_2_0 = "2.2.0"
    v_2_1_1 = "2.1.1"
    v_2_1_0 = "2.1.0"
    v_2_0_0 = "2.0.0"
    v_1_1_0 = "1.1.0"
    v_1_0_0 = "1.0.0"

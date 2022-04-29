from enum import Enum


class VersionEnum(str, Enum):
    VALUE_0 = "2.2.1"
    VALUE_1 = "2.2.0"
    VALUE_2 = "2.1.1"
    VALUE_3 = "2.1.0"
    VALUE_4 = "2.0.0"
    VALUE_5 = "1.1.0"
    VALUE_6 = "1.0.0"

    def __str__(self) -> str:
        return str(self.value)

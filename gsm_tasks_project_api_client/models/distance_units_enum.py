from enum import Enum


class DistanceUnitsEnum(str, Enum):
    KILOMETERS = "kilometers"
    MILES = "miles"

    def __str__(self) -> str:
        return str(self.value)

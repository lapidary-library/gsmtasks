from enum import Enum


class ObjectiveEnum(str, Enum):
    VEHICLES = "vehicles"
    TRANSPORT_TIME = "transport_time"
    COMPLETION_TIME = "completion_time"

    def __str__(self) -> str:
        return str(self.value)

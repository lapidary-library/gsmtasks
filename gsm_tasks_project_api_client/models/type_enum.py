from enum import Enum


class TypeEnum(str, Enum):
    SERVICE = "service"
    DELIVERY = "delivery"

    def __str__(self) -> str:
        return str(self.value)

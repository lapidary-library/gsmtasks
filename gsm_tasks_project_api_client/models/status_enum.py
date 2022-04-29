from enum import Enum


class StatusEnum(str, Enum):
    ON_DUTY = "on_duty"
    OFF_DUTY = "off_duty"

    def __str__(self) -> str:
        return str(self.value)

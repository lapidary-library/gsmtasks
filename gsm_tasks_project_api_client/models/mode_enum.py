from enum import Enum


class ModeEnum(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"

    def __str__(self) -> str:
        return str(self.value)

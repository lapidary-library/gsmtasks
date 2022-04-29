from enum import Enum


class WorkingStateListMode(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"

    def __str__(self) -> str:
        return str(self.value)

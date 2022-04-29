from enum import Enum


class UsersOnDutyLogListMode(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"

    def __str__(self) -> str:
        return str(self.value)

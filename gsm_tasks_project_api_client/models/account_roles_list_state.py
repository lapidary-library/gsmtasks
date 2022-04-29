from enum import Enum


class AccountRolesListState(str, Enum):
    INACTIVE = "inactive"
    ACTIVE = "active"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)

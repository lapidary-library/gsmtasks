from enum import Enum


class WebhooksListState(str, Enum):
    INACTIVE = "inactive"
    ACTIVE = "active"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)

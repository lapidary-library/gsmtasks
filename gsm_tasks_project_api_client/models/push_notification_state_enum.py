from enum import Enum


class PushNotificationStateEnum(str, Enum):
    QUEUED = "queued"
    PENDING = "pending"
    FAILED = "failed"
    SENT = "sent"

    def __str__(self) -> str:
        return str(self.value)

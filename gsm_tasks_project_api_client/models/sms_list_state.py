from enum import Enum


class SmsListState(str, Enum):
    QUEUED = "queued"
    OVER_QUOTA = "over_quota"
    SENT = "sent"
    FAILED = "failed"
    RECEIVED = "received"

    def __str__(self) -> str:
        return str(self.value)

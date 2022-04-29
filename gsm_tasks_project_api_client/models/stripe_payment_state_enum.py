from enum import Enum


class StripePaymentStateEnum(str, Enum):
    DRAFT = "draft"
    FAILED = "failed"
    SAVED = "saved"
    SETTLED = "settled"
    REJECTED = "rejected"
    RETRIED = "retried"
    CANCELLED = "cancelled"

    def __str__(self) -> str:
        return str(self.value)

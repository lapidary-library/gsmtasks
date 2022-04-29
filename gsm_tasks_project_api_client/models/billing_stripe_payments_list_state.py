from enum import Enum


class BillingStripePaymentsListState(str, Enum):
    DRAFT = "draft"
    FAILED = "failed"
    SAVED = "saved"
    SETTLED = "settled"
    REJECTED = "rejected"
    RETRIED = "retried"
    CANCELLED = "cancelled"

    def __str__(self) -> str:
        return str(self.value)

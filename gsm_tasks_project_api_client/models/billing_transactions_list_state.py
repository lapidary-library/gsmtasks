from enum import Enum


class BillingTransactionsListState(str, Enum):
    DRAFT = "draft"
    FAILED = "failed"
    SAVED = "saved"
    SETTLED = "settled"
    REJECTED = "rejected"
    VOIDED = "voided"
    REFUNDED = "refunded"
    RETRIED = "retried"
    CANCELLED = "cancelled"
    IMPORTED = "imported"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class BillingInvoicesListState(str, Enum):
    DRAFT = "draft"
    CONFIRMED = "confirmed"
    OVERDUE = "overdue"
    PAID = "paid"
    CANCELLED = "cancelled"

    def __str__(self) -> str:
        return str(self.value)

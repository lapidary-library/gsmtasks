from enum import Enum


class BillingInvoicesListBillingMethod(str, Enum):
    BRAINTREE = "braintree"
    INVOICE = "invoice"
    STRIPE = "stripe"

    def __str__(self) -> str:
        return str(self.value)

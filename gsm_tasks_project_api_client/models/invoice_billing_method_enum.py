from enum import Enum


class InvoiceBillingMethodEnum(str, Enum):
    BRAINTREE = "braintree"
    INVOICE = "invoice"
    STRIPE = "stripe"

    def __str__(self) -> str:
        return str(self.value)

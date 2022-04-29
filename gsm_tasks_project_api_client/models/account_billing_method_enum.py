from enum import Enum


class AccountBillingMethodEnum(str, Enum):
    BRAINTREE = "braintree"
    FREE = "free"
    INVOICE = "invoice"
    STRIPE = "stripe"
    TRIAL = "trial"

    def __str__(self) -> str:
        return str(self.value)

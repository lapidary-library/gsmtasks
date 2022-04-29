from enum import Enum


class BillingStripePaymentsListStripeState(str, Enum):
    REQUIRES_PAYMENT_METHOD = "requires_payment_method"
    REQUIRES_CONFIRMATION = "requires_confirmation"
    REQUIRES_CAPTURE = "requires_capture"
    REQUIRES_ACTION = "requires_action"
    PROCESSING = "processing"
    SUCCEEDED = "succeeded"
    CANCELED = "canceled"

    def __str__(self) -> str:
        return str(self.value)

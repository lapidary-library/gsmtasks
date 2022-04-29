from enum import Enum


class BillingStripePaymentsRetrieveFormat(str, Enum):
    JSON = "json"
    XLSX = "xlsx"

    def __str__(self) -> str:
        return str(self.value)

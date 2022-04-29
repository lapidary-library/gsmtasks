from enum import Enum


class SmsListProvider(str, Enum):
    TWILIO = "twilio"
    SMSAPI = "smsapi"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class SignaturesListSource(str, Enum):
    WEB = "web"
    MOBILE = "mobile"
    INTEGRATION = "integration"

    def __str__(self) -> str:
        return str(self.value)

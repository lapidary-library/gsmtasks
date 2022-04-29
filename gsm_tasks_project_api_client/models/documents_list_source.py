from enum import Enum


class DocumentsListSource(str, Enum):
    WEB = "web"
    MOBILE = "mobile"
    INTEGRATION = "integration"

    def __str__(self) -> str:
        return str(self.value)

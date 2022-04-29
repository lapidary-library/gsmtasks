from enum import Enum


class FileUploadsListSource(str, Enum):
    WEB = "web"
    MOBILE = "mobile"
    INTEGRATION = "integration"

    def __str__(self) -> str:
        return str(self.value)

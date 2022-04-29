from enum import Enum


class NotificationsListRecipient(str, Enum):
    ACCOUNT = "account"
    ASSIGNEE = "assignee"
    ORDERER = "orderer"
    CONTACT = "contact"
    CLIENT = "client"

    def __str__(self) -> str:
        return str(self.value)

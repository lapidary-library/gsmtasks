import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.state_a81_enum import StateA81Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Email")


@attr.s(auto_attribs=True)
class Email:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        state (StateA81Enum):
        notification (str):
        sender (str):
        subject (str):
        message (str):
        sent_at (datetime.datetime):
        failed_at (datetime.datetime):
        received_at (datetime.datetime):
        created_at (datetime.datetime):
        external_id (Union[Unset, str]):
        from_email (Union[Unset, str]):
        reply_to_email (Union[Unset, str]):
        to_emails (Union[Unset, List[str]]):
    """

    id: str
    url: str
    account: str
    state: StateA81Enum
    notification: str
    sender: str
    subject: str
    message: str
    sent_at: datetime.datetime
    failed_at: datetime.datetime
    received_at: datetime.datetime
    created_at: datetime.datetime
    external_id: Union[Unset, str] = UNSET
    from_email: Union[Unset, str] = UNSET
    reply_to_email: Union[Unset, str] = UNSET
    to_emails: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        state = self.state.value

        notification = self.notification
        sender = self.sender
        subject = self.subject
        message = self.message
        sent_at = self.sent_at.isoformat()

        failed_at = self.failed_at.isoformat()

        received_at = self.received_at.isoformat()

        created_at = self.created_at.isoformat()

        external_id = self.external_id
        from_email = self.from_email
        reply_to_email = self.reply_to_email
        to_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.to_emails, Unset):
            to_emails = self.to_emails

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "state": state,
                "notification": notification,
                "sender": sender,
                "subject": subject,
                "message": message,
                "sent_at": sent_at,
                "failed_at": failed_at,
                "received_at": received_at,
                "created_at": created_at,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if from_email is not UNSET:
            field_dict["from_email"] = from_email
        if reply_to_email is not UNSET:
            field_dict["reply_to_email"] = reply_to_email
        if to_emails is not UNSET:
            field_dict["to_emails"] = to_emails

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        state = (None, str(self.state.value).encode(), "text/plain")

        notification = (
            self.notification
            if isinstance(self.notification, Unset)
            else (None, str(self.notification).encode(), "text/plain")
        )
        sender = self.sender if isinstance(self.sender, Unset) else (None, str(self.sender).encode(), "text/plain")
        subject = self.subject if isinstance(self.subject, Unset) else (None, str(self.subject).encode(), "text/plain")
        message = self.message if isinstance(self.message, Unset) else (None, str(self.message).encode(), "text/plain")
        sent_at = self.sent_at.isoformat().encode()

        failed_at = self.failed_at.isoformat().encode()

        received_at = self.received_at.isoformat().encode()

        created_at = self.created_at.isoformat().encode()

        external_id = (
            self.external_id
            if isinstance(self.external_id, Unset)
            else (None, str(self.external_id).encode(), "text/plain")
        )
        from_email = (
            self.from_email
            if isinstance(self.from_email, Unset)
            else (None, str(self.from_email).encode(), "text/plain")
        )
        reply_to_email = (
            self.reply_to_email
            if isinstance(self.reply_to_email, Unset)
            else (None, str(self.reply_to_email).encode(), "text/plain")
        )
        to_emails: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.to_emails, Unset):
            _temp_to_emails = self.to_emails
            to_emails = (None, json.dumps(_temp_to_emails).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "state": state,
                "notification": notification,
                "sender": sender,
                "subject": subject,
                "message": message,
                "sent_at": sent_at,
                "failed_at": failed_at,
                "received_at": received_at,
                "created_at": created_at,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if from_email is not UNSET:
            field_dict["from_email"] = from_email
        if reply_to_email is not UNSET:
            field_dict["reply_to_email"] = reply_to_email
        if to_emails is not UNSET:
            field_dict["to_emails"] = to_emails

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        state = StateA81Enum(d.pop("state"))

        notification = d.pop("notification")

        sender = d.pop("sender")

        subject = d.pop("subject")

        message = d.pop("message")

        sent_at = isoparse(d.pop("sent_at"))

        failed_at = isoparse(d.pop("failed_at"))

        received_at = isoparse(d.pop("received_at"))

        created_at = isoparse(d.pop("created_at"))

        external_id = d.pop("external_id", UNSET)

        from_email = d.pop("from_email", UNSET)

        reply_to_email = d.pop("reply_to_email", UNSET)

        to_emails = cast(List[str], d.pop("to_emails", UNSET))

        email = cls(
            id=id,
            url=url,
            account=account,
            state=state,
            notification=notification,
            sender=sender,
            subject=subject,
            message=message,
            sent_at=sent_at,
            failed_at=failed_at,
            received_at=received_at,
            created_at=created_at,
            external_id=external_id,
            from_email=from_email,
            reply_to_email=reply_to_email,
            to_emails=to_emails,
        )

        email.additional_properties = d
        return email

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

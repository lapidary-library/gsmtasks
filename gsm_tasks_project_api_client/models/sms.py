import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.state_a81_enum import StateA81Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SMS")


@attr.s(auto_attribs=True)
class SMS:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        state (StateA81Enum):
        notification (str):
        sender (str):
        phone (str):
        sent_at (datetime.datetime):
        failed_at (datetime.datetime):
        received_at (datetime.datetime):
        created_at (datetime.datetime):
        external_id (Union[Unset, str]):
        alphanumeric_sender_id (Union[Unset, str]):
        message (Union[Unset, None, str]):
        segments_count (Union[Unset, int]):
        error (Union[Unset, None, str]):
    """

    id: str
    url: str
    account: str
    state: StateA81Enum
    notification: str
    sender: str
    phone: str
    sent_at: datetime.datetime
    failed_at: datetime.datetime
    received_at: datetime.datetime
    created_at: datetime.datetime
    external_id: Union[Unset, str] = UNSET
    alphanumeric_sender_id: Union[Unset, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    segments_count: Union[Unset, int] = UNSET
    error: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        state = self.state.value

        notification = self.notification
        sender = self.sender
        phone = self.phone
        sent_at = self.sent_at.isoformat()

        failed_at = self.failed_at.isoformat()

        received_at = self.received_at.isoformat()

        created_at = self.created_at.isoformat()

        external_id = self.external_id
        alphanumeric_sender_id = self.alphanumeric_sender_id
        message = self.message
        segments_count = self.segments_count
        error = self.error

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
                "phone": phone,
                "sent_at": sent_at,
                "failed_at": failed_at,
                "received_at": received_at,
                "created_at": created_at,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if alphanumeric_sender_id is not UNSET:
            field_dict["alphanumeric_sender_id"] = alphanumeric_sender_id
        if message is not UNSET:
            field_dict["message"] = message
        if segments_count is not UNSET:
            field_dict["segments_count"] = segments_count
        if error is not UNSET:
            field_dict["error"] = error

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
        phone = self.phone if isinstance(self.phone, Unset) else (None, str(self.phone).encode(), "text/plain")
        sent_at = self.sent_at.isoformat().encode()

        failed_at = self.failed_at.isoformat().encode()

        received_at = self.received_at.isoformat().encode()

        created_at = self.created_at.isoformat().encode()

        external_id = (
            self.external_id
            if isinstance(self.external_id, Unset)
            else (None, str(self.external_id).encode(), "text/plain")
        )
        alphanumeric_sender_id = (
            self.alphanumeric_sender_id
            if isinstance(self.alphanumeric_sender_id, Unset)
            else (None, str(self.alphanumeric_sender_id).encode(), "text/plain")
        )
        message = self.message if isinstance(self.message, Unset) else (None, str(self.message).encode(), "text/plain")
        segments_count = (
            self.segments_count
            if isinstance(self.segments_count, Unset)
            else (None, str(self.segments_count).encode(), "text/plain")
        )
        error = self.error if isinstance(self.error, Unset) else (None, str(self.error).encode(), "text/plain")

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
                "phone": phone,
                "sent_at": sent_at,
                "failed_at": failed_at,
                "received_at": received_at,
                "created_at": created_at,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if alphanumeric_sender_id is not UNSET:
            field_dict["alphanumeric_sender_id"] = alphanumeric_sender_id
        if message is not UNSET:
            field_dict["message"] = message
        if segments_count is not UNSET:
            field_dict["segments_count"] = segments_count
        if error is not UNSET:
            field_dict["error"] = error

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

        phone = d.pop("phone")

        sent_at = isoparse(d.pop("sent_at"))

        failed_at = isoparse(d.pop("failed_at"))

        received_at = isoparse(d.pop("received_at"))

        created_at = isoparse(d.pop("created_at"))

        external_id = d.pop("external_id", UNSET)

        alphanumeric_sender_id = d.pop("alphanumeric_sender_id", UNSET)

        message = d.pop("message", UNSET)

        segments_count = d.pop("segments_count", UNSET)

        error = d.pop("error", UNSET)

        sms = cls(
            id=id,
            url=url,
            account=account,
            state=state,
            notification=notification,
            sender=sender,
            phone=phone,
            sent_at=sent_at,
            failed_at=failed_at,
            received_at=received_at,
            created_at=created_at,
            external_id=external_id,
            alphanumeric_sender_id=alphanumeric_sender_id,
            message=message,
            segments_count=segments_count,
            error=error,
        )

        sms.additional_properties = d
        return sms

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

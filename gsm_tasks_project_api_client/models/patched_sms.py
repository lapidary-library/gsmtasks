import datetime
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.state_a81_enum import StateA81Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSMS")


@attr.s(auto_attribs=True)
class PatchedSMS:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        account (Union[Unset, str]):
        external_id (Union[Unset, str]):
        state (Union[Unset, StateA81Enum]):
        notification (Union[Unset, str]):
        sender (Union[Unset, str]):
        alphanumeric_sender_id (Union[Unset, str]):
        phone (Union[Unset, str]):
        message (Union[Unset, None, str]):
        segments_count (Union[Unset, int]):
        error (Union[Unset, None, str]):
        sent_at (Union[Unset, datetime.datetime]):
        failed_at (Union[Unset, datetime.datetime]):
        received_at (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    state: Union[Unset, StateA81Enum] = UNSET
    notification: Union[Unset, str] = UNSET
    sender: Union[Unset, str] = UNSET
    alphanumeric_sender_id: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    segments_count: Union[Unset, int] = UNSET
    error: Union[Unset, None, str] = UNSET
    sent_at: Union[Unset, datetime.datetime] = UNSET
    failed_at: Union[Unset, datetime.datetime] = UNSET
    received_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        external_id = self.external_id
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        notification = self.notification
        sender = self.sender
        alphanumeric_sender_id = self.alphanumeric_sender_id
        phone = self.phone
        message = self.message
        segments_count = self.segments_count
        error = self.error
        sent_at: Union[Unset, str] = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat()

        failed_at: Union[Unset, str] = UNSET
        if not isinstance(self.failed_at, Unset):
            failed_at = self.failed_at.isoformat()

        received_at: Union[Unset, str] = UNSET
        if not isinstance(self.received_at, Unset):
            received_at = self.received_at.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if account is not UNSET:
            field_dict["account"] = account
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if state is not UNSET:
            field_dict["state"] = state
        if notification is not UNSET:
            field_dict["notification"] = notification
        if sender is not UNSET:
            field_dict["sender"] = sender
        if alphanumeric_sender_id is not UNSET:
            field_dict["alphanumeric_sender_id"] = alphanumeric_sender_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if message is not UNSET:
            field_dict["message"] = message
        if segments_count is not UNSET:
            field_dict["segments_count"] = segments_count
        if error is not UNSET:
            field_dict["error"] = error
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at
        if failed_at is not UNSET:
            field_dict["failed_at"] = failed_at
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        external_id = (
            self.external_id
            if isinstance(self.external_id, Unset)
            else (None, str(self.external_id).encode(), "text/plain")
        )
        state: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.state, Unset):
            state = (None, str(self.state.value).encode(), "text/plain")

        notification = (
            self.notification
            if isinstance(self.notification, Unset)
            else (None, str(self.notification).encode(), "text/plain")
        )
        sender = self.sender if isinstance(self.sender, Unset) else (None, str(self.sender).encode(), "text/plain")
        alphanumeric_sender_id = (
            self.alphanumeric_sender_id
            if isinstance(self.alphanumeric_sender_id, Unset)
            else (None, str(self.alphanumeric_sender_id).encode(), "text/plain")
        )
        phone = self.phone if isinstance(self.phone, Unset) else (None, str(self.phone).encode(), "text/plain")
        message = self.message if isinstance(self.message, Unset) else (None, str(self.message).encode(), "text/plain")
        segments_count = (
            self.segments_count
            if isinstance(self.segments_count, Unset)
            else (None, str(self.segments_count).encode(), "text/plain")
        )
        error = self.error if isinstance(self.error, Unset) else (None, str(self.error).encode(), "text/plain")
        sent_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat().encode()

        failed_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.failed_at, Unset):
            failed_at = self.failed_at.isoformat().encode()

        received_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.received_at, Unset):
            received_at = self.received_at.isoformat().encode()

        created_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if account is not UNSET:
            field_dict["account"] = account
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if state is not UNSET:
            field_dict["state"] = state
        if notification is not UNSET:
            field_dict["notification"] = notification
        if sender is not UNSET:
            field_dict["sender"] = sender
        if alphanumeric_sender_id is not UNSET:
            field_dict["alphanumeric_sender_id"] = alphanumeric_sender_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if message is not UNSET:
            field_dict["message"] = message
        if segments_count is not UNSET:
            field_dict["segments_count"] = segments_count
        if error is not UNSET:
            field_dict["error"] = error
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at
        if failed_at is not UNSET:
            field_dict["failed_at"] = failed_at
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        account = d.pop("account", UNSET)

        external_id = d.pop("external_id", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, StateA81Enum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = StateA81Enum(_state)

        notification = d.pop("notification", UNSET)

        sender = d.pop("sender", UNSET)

        alphanumeric_sender_id = d.pop("alphanumeric_sender_id", UNSET)

        phone = d.pop("phone", UNSET)

        message = d.pop("message", UNSET)

        segments_count = d.pop("segments_count", UNSET)

        error = d.pop("error", UNSET)

        _sent_at = d.pop("sent_at", UNSET)
        sent_at: Union[Unset, datetime.datetime]
        if isinstance(_sent_at, Unset):
            sent_at = UNSET
        else:
            sent_at = isoparse(_sent_at)

        _failed_at = d.pop("failed_at", UNSET)
        failed_at: Union[Unset, datetime.datetime]
        if isinstance(_failed_at, Unset):
            failed_at = UNSET
        else:
            failed_at = isoparse(_failed_at)

        _received_at = d.pop("received_at", UNSET)
        received_at: Union[Unset, datetime.datetime]
        if isinstance(_received_at, Unset):
            received_at = UNSET
        else:
            received_at = isoparse(_received_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        patched_sms = cls(
            id=id,
            url=url,
            account=account,
            external_id=external_id,
            state=state,
            notification=notification,
            sender=sender,
            alphanumeric_sender_id=alphanumeric_sender_id,
            phone=phone,
            message=message,
            segments_count=segments_count,
            error=error,
            sent_at=sent_at,
            failed_at=failed_at,
            received_at=received_at,
            created_at=created_at,
        )

        patched_sms.additional_properties = d
        return patched_sms

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

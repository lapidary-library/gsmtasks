import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.event_enum import EventEnum
from ..models.push_notification_state_enum import PushNotificationStateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PushNotification")


@attr.s(auto_attribs=True)
class PushNotification:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        state (PushNotificationStateEnum):
        notification (str):
        recipient (str):
        task (str):
        message (str):
        pending_at (datetime.datetime):
        failed_at (datetime.datetime):
        sent_at (datetime.datetime):
        created_at (datetime.datetime):
        external_id (Union[Unset, None, str]):
        event (Union[BlankEnum, EventEnum, None, Unset]):
        subject (Union[Unset, str]):
        error (Union[Unset, None, str]):
    """

    id: str
    url: str
    account: str
    state: PushNotificationStateEnum
    notification: str
    recipient: str
    task: str
    message: str
    pending_at: datetime.datetime
    failed_at: datetime.datetime
    sent_at: datetime.datetime
    created_at: datetime.datetime
    external_id: Union[Unset, None, str] = UNSET
    event: Union[BlankEnum, EventEnum, None, Unset] = UNSET
    subject: Union[Unset, str] = UNSET
    error: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        state = self.state.value

        notification = self.notification
        recipient = self.recipient
        task = self.task
        message = self.message
        pending_at = self.pending_at.isoformat()

        failed_at = self.failed_at.isoformat()

        sent_at = self.sent_at.isoformat()

        created_at = self.created_at.isoformat()

        external_id = self.external_id
        event: Union[None, Unset, str]
        if isinstance(self.event, Unset):
            event = UNSET
        elif self.event is None:
            event = None

        elif isinstance(self.event, EventEnum):
            event = UNSET
            if not isinstance(self.event, Unset):
                event = self.event.value

        elif isinstance(self.event, BlankEnum):
            event = UNSET
            if not isinstance(self.event, Unset):
                event = self.event.value

        else:
            event = self.event

        subject = self.subject
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
                "recipient": recipient,
                "task": task,
                "message": message,
                "pending_at": pending_at,
                "failed_at": failed_at,
                "sent_at": sent_at,
                "created_at": created_at,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if event is not UNSET:
            field_dict["event"] = event
        if subject is not UNSET:
            field_dict["subject"] = subject
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
        recipient = (
            self.recipient if isinstance(self.recipient, Unset) else (None, str(self.recipient).encode(), "text/plain")
        )
        task = self.task if isinstance(self.task, Unset) else (None, str(self.task).encode(), "text/plain")
        message = self.message if isinstance(self.message, Unset) else (None, str(self.message).encode(), "text/plain")
        pending_at = self.pending_at.isoformat().encode()

        failed_at = self.failed_at.isoformat().encode()

        sent_at = self.sent_at.isoformat().encode()

        created_at = self.created_at.isoformat().encode()

        external_id = (
            self.external_id
            if isinstance(self.external_id, Unset)
            else (None, str(self.external_id).encode(), "text/plain")
        )
        event: Union[None, Unset, str]
        if isinstance(self.event, Unset):
            event = UNSET
        elif self.event is None:
            event = None

        elif isinstance(self.event, EventEnum):
            event = UNSET
            if not isinstance(self.event, Unset):
                event = (None, str(self.event.value).encode(), "text/plain")

        elif isinstance(self.event, BlankEnum):
            event = UNSET
            if not isinstance(self.event, Unset):
                event = (None, str(self.event.value).encode(), "text/plain")

        else:
            event = self.event

        subject = self.subject if isinstance(self.subject, Unset) else (None, str(self.subject).encode(), "text/plain")
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
                "recipient": recipient,
                "task": task,
                "message": message,
                "pending_at": pending_at,
                "failed_at": failed_at,
                "sent_at": sent_at,
                "created_at": created_at,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if event is not UNSET:
            field_dict["event"] = event
        if subject is not UNSET:
            field_dict["subject"] = subject
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        state = PushNotificationStateEnum(d.pop("state"))

        notification = d.pop("notification")

        recipient = d.pop("recipient")

        task = d.pop("task")

        message = d.pop("message")

        pending_at = isoparse(d.pop("pending_at"))

        failed_at = isoparse(d.pop("failed_at"))

        sent_at = isoparse(d.pop("sent_at"))

        created_at = isoparse(d.pop("created_at"))

        external_id = d.pop("external_id", UNSET)

        def _parse_event(data: object) -> Union[BlankEnum, EventEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _event_type_0 = data
                event_type_0: Union[Unset, EventEnum]
                if isinstance(_event_type_0, Unset):
                    event_type_0 = UNSET
                else:
                    event_type_0 = EventEnum(_event_type_0)

                return event_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _event_type_1 = data
                event_type_1: Union[Unset, BlankEnum]
                if isinstance(_event_type_1, Unset):
                    event_type_1 = UNSET
                else:
                    event_type_1 = BlankEnum(_event_type_1)

                return event_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, EventEnum, None, Unset], data)

        event = _parse_event(d.pop("event", UNSET))

        subject = d.pop("subject", UNSET)

        error = d.pop("error", UNSET)

        push_notification = cls(
            id=id,
            url=url,
            account=account,
            state=state,
            notification=notification,
            recipient=recipient,
            task=task,
            message=message,
            pending_at=pending_at,
            failed_at=failed_at,
            sent_at=sent_at,
            created_at=created_at,
            external_id=external_id,
            event=event,
            subject=subject,
            error=error,
        )

        push_notification.additional_properties = d
        return push_notification

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

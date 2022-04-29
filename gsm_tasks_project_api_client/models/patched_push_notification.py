import datetime
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.event_enum import EventEnum
from ..models.push_notification_state_enum import PushNotificationStateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedPushNotification")


@attr.s(auto_attribs=True)
class PatchedPushNotification:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        account (Union[Unset, str]):
        external_id (Union[Unset, None, str]):
        state (Union[Unset, PushNotificationStateEnum]):
        notification (Union[Unset, str]):
        recipient (Union[Unset, str]):
        task (Union[Unset, str]):
        event (Union[BlankEnum, EventEnum, None, Unset]):
        subject (Union[Unset, str]):
        message (Union[Unset, str]):
        error (Union[Unset, None, str]):
        pending_at (Union[Unset, datetime.datetime]):
        failed_at (Union[Unset, datetime.datetime]):
        sent_at (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    state: Union[Unset, PushNotificationStateEnum] = UNSET
    notification: Union[Unset, str] = UNSET
    recipient: Union[Unset, str] = UNSET
    task: Union[Unset, str] = UNSET
    event: Union[BlankEnum, EventEnum, None, Unset] = UNSET
    subject: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    error: Union[Unset, None, str] = UNSET
    pending_at: Union[Unset, datetime.datetime] = UNSET
    failed_at: Union[Unset, datetime.datetime] = UNSET
    sent_at: Union[Unset, datetime.datetime] = UNSET
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
        recipient = self.recipient
        task = self.task
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
        message = self.message
        error = self.error
        pending_at: Union[Unset, str] = UNSET
        if not isinstance(self.pending_at, Unset):
            pending_at = self.pending_at.isoformat()

        failed_at: Union[Unset, str] = UNSET
        if not isinstance(self.failed_at, Unset):
            failed_at = self.failed_at.isoformat()

        sent_at: Union[Unset, str] = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat()

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
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if task is not UNSET:
            field_dict["task"] = task
        if event is not UNSET:
            field_dict["event"] = event
        if subject is not UNSET:
            field_dict["subject"] = subject
        if message is not UNSET:
            field_dict["message"] = message
        if error is not UNSET:
            field_dict["error"] = error
        if pending_at is not UNSET:
            field_dict["pending_at"] = pending_at
        if failed_at is not UNSET:
            field_dict["failed_at"] = failed_at
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at
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
        recipient = (
            self.recipient if isinstance(self.recipient, Unset) else (None, str(self.recipient).encode(), "text/plain")
        )
        task = self.task if isinstance(self.task, Unset) else (None, str(self.task).encode(), "text/plain")
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
        message = self.message if isinstance(self.message, Unset) else (None, str(self.message).encode(), "text/plain")
        error = self.error if isinstance(self.error, Unset) else (None, str(self.error).encode(), "text/plain")
        pending_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.pending_at, Unset):
            pending_at = self.pending_at.isoformat().encode()

        failed_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.failed_at, Unset):
            failed_at = self.failed_at.isoformat().encode()

        sent_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat().encode()

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
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if task is not UNSET:
            field_dict["task"] = task
        if event is not UNSET:
            field_dict["event"] = event
        if subject is not UNSET:
            field_dict["subject"] = subject
        if message is not UNSET:
            field_dict["message"] = message
        if error is not UNSET:
            field_dict["error"] = error
        if pending_at is not UNSET:
            field_dict["pending_at"] = pending_at
        if failed_at is not UNSET:
            field_dict["failed_at"] = failed_at
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at
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
        state: Union[Unset, PushNotificationStateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PushNotificationStateEnum(_state)

        notification = d.pop("notification", UNSET)

        recipient = d.pop("recipient", UNSET)

        task = d.pop("task", UNSET)

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

        message = d.pop("message", UNSET)

        error = d.pop("error", UNSET)

        _pending_at = d.pop("pending_at", UNSET)
        pending_at: Union[Unset, datetime.datetime]
        if isinstance(_pending_at, Unset):
            pending_at = UNSET
        else:
            pending_at = isoparse(_pending_at)

        _failed_at = d.pop("failed_at", UNSET)
        failed_at: Union[Unset, datetime.datetime]
        if isinstance(_failed_at, Unset):
            failed_at = UNSET
        else:
            failed_at = isoparse(_failed_at)

        _sent_at = d.pop("sent_at", UNSET)
        sent_at: Union[Unset, datetime.datetime]
        if isinstance(_sent_at, Unset):
            sent_at = UNSET
        else:
            sent_at = isoparse(_sent_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        patched_push_notification = cls(
            id=id,
            url=url,
            account=account,
            external_id=external_id,
            state=state,
            notification=notification,
            recipient=recipient,
            task=task,
            event=event,
            subject=subject,
            message=message,
            error=error,
            pending_at=pending_at,
            failed_at=failed_at,
            sent_at=sent_at,
            created_at=created_at,
        )

        patched_push_notification.additional_properties = d
        return patched_push_notification

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

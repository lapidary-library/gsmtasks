import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.assignee_proximity_enum import AssigneeProximityEnum
from ..models.blank_enum import BlankEnum
from ..models.event_enum import EventEnum
from ..models.recipient_enum import RecipientEnum
from ..models.state_ef_4_enum import StateEf4Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Notification")


@attr.s(auto_attribs=True)
class Notification:
    """
    Attributes:
        id (str):
        url (str):
        method (str):
        task (str):
        sms_count (int):
        via_app (bool):
        via_email (bool):
        via_sms (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        template (Union[Unset, None, str]):
        event (Union[BlankEnum, EventEnum, None, Unset]):
        state (Union[BlankEnum, None, StateEf4Enum, Unset]):
        assignee_proximity (Union[AssigneeProximityEnum, BlankEnum, None, Unset]):
        recipient (Union[BlankEnum, None, RecipientEnum, Unset]):
        emails (Union[Unset, None, List[str]]):
        phones (Union[Unset, List[str]]):
        message (Union[Unset, str]):
        add_tracking_link (Union[Unset, bool]):
        sent_at (Union[Unset, None, datetime.datetime]):
    """

    id: str
    url: str
    method: str
    task: str
    sms_count: int
    via_app: bool
    via_email: bool
    via_sms: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    template: Union[Unset, None, str] = UNSET
    event: Union[BlankEnum, EventEnum, None, Unset] = UNSET
    state: Union[BlankEnum, None, StateEf4Enum, Unset] = UNSET
    assignee_proximity: Union[AssigneeProximityEnum, BlankEnum, None, Unset] = UNSET
    recipient: Union[BlankEnum, None, RecipientEnum, Unset] = UNSET
    emails: Union[Unset, None, List[str]] = UNSET
    phones: Union[Unset, List[str]] = UNSET
    message: Union[Unset, str] = UNSET
    add_tracking_link: Union[Unset, bool] = UNSET
    sent_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        method = self.method
        task = self.task
        sms_count = self.sms_count
        via_app = self.via_app
        via_email = self.via_email
        via_sms = self.via_sms
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        template = self.template
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

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        elif self.state is None:
            state = None

        elif isinstance(self.state, StateEf4Enum):
            state = UNSET
            if not isinstance(self.state, Unset):
                state = self.state.value

        elif isinstance(self.state, BlankEnum):
            state = UNSET
            if not isinstance(self.state, Unset):
                state = self.state.value

        else:
            state = self.state

        assignee_proximity: Union[None, Unset, str]
        if isinstance(self.assignee_proximity, Unset):
            assignee_proximity = UNSET
        elif self.assignee_proximity is None:
            assignee_proximity = None

        elif isinstance(self.assignee_proximity, AssigneeProximityEnum):
            assignee_proximity = UNSET
            if not isinstance(self.assignee_proximity, Unset):
                assignee_proximity = self.assignee_proximity.value

        elif isinstance(self.assignee_proximity, BlankEnum):
            assignee_proximity = UNSET
            if not isinstance(self.assignee_proximity, Unset):
                assignee_proximity = self.assignee_proximity.value

        else:
            assignee_proximity = self.assignee_proximity

        recipient: Union[None, Unset, str]
        if isinstance(self.recipient, Unset):
            recipient = UNSET
        elif self.recipient is None:
            recipient = None

        elif isinstance(self.recipient, RecipientEnum):
            recipient = UNSET
            if not isinstance(self.recipient, Unset):
                recipient = self.recipient.value

        elif isinstance(self.recipient, BlankEnum):
            recipient = UNSET
            if not isinstance(self.recipient, Unset):
                recipient = self.recipient.value

        else:
            recipient = self.recipient

        emails: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.emails, Unset):
            if self.emails is None:
                emails = None
            else:
                emails = self.emails

        phones: Union[Unset, List[str]] = UNSET
        if not isinstance(self.phones, Unset):
            phones = self.phones

        message = self.message
        add_tracking_link = self.add_tracking_link
        sent_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat() if self.sent_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "method": method,
                "task": task,
                "sms_count": sms_count,
                "via_app": via_app,
                "via_email": via_email,
                "via_sms": via_sms,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if template is not UNSET:
            field_dict["template"] = template
        if event is not UNSET:
            field_dict["event"] = event
        if state is not UNSET:
            field_dict["state"] = state
        if assignee_proximity is not UNSET:
            field_dict["assignee_proximity"] = assignee_proximity
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if emails is not UNSET:
            field_dict["emails"] = emails
        if phones is not UNSET:
            field_dict["phones"] = phones
        if message is not UNSET:
            field_dict["message"] = message
        if add_tracking_link is not UNSET:
            field_dict["add_tracking_link"] = add_tracking_link
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        method = self.method if isinstance(self.method, Unset) else (None, str(self.method).encode(), "text/plain")
        task = self.task if isinstance(self.task, Unset) else (None, str(self.task).encode(), "text/plain")
        sms_count = (
            self.sms_count if isinstance(self.sms_count, Unset) else (None, str(self.sms_count).encode(), "text/plain")
        )
        via_app = self.via_app if isinstance(self.via_app, Unset) else (None, str(self.via_app).encode(), "text/plain")
        via_email = (
            self.via_email if isinstance(self.via_email, Unset) else (None, str(self.via_email).encode(), "text/plain")
        )
        via_sms = self.via_sms if isinstance(self.via_sms, Unset) else (None, str(self.via_sms).encode(), "text/plain")
        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        template = (
            self.template if isinstance(self.template, Unset) else (None, str(self.template).encode(), "text/plain")
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

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        elif self.state is None:
            state = None

        elif isinstance(self.state, StateEf4Enum):
            state = UNSET
            if not isinstance(self.state, Unset):
                state = (None, str(self.state.value).encode(), "text/plain")

        elif isinstance(self.state, BlankEnum):
            state = UNSET
            if not isinstance(self.state, Unset):
                state = (None, str(self.state.value).encode(), "text/plain")

        else:
            state = self.state

        assignee_proximity: Union[None, Unset, str]
        if isinstance(self.assignee_proximity, Unset):
            assignee_proximity = UNSET
        elif self.assignee_proximity is None:
            assignee_proximity = None

        elif isinstance(self.assignee_proximity, AssigneeProximityEnum):
            assignee_proximity = UNSET
            if not isinstance(self.assignee_proximity, Unset):
                assignee_proximity = (None, str(self.assignee_proximity.value).encode(), "text/plain")

        elif isinstance(self.assignee_proximity, BlankEnum):
            assignee_proximity = UNSET
            if not isinstance(self.assignee_proximity, Unset):
                assignee_proximity = (None, str(self.assignee_proximity.value).encode(), "text/plain")

        else:
            assignee_proximity = self.assignee_proximity

        recipient: Union[None, Unset, str]
        if isinstance(self.recipient, Unset):
            recipient = UNSET
        elif self.recipient is None:
            recipient = None

        elif isinstance(self.recipient, RecipientEnum):
            recipient = UNSET
            if not isinstance(self.recipient, Unset):
                recipient = (None, str(self.recipient.value).encode(), "text/plain")

        elif isinstance(self.recipient, BlankEnum):
            recipient = UNSET
            if not isinstance(self.recipient, Unset):
                recipient = (None, str(self.recipient.value).encode(), "text/plain")

        else:
            recipient = self.recipient

        emails: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.emails, Unset):
            if self.emails is None:
                emails = None
            else:
                _temp_emails = self.emails
                emails = (None, json.dumps(_temp_emails).encode(), "application/json")

        phones: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.phones, Unset):
            _temp_phones = self.phones
            phones = (None, json.dumps(_temp_phones).encode(), "application/json")

        message = self.message if isinstance(self.message, Unset) else (None, str(self.message).encode(), "text/plain")
        add_tracking_link = (
            self.add_tracking_link
            if isinstance(self.add_tracking_link, Unset)
            else (None, str(self.add_tracking_link).encode(), "text/plain")
        )
        sent_at: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat().encode() if self.sent_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "method": method,
                "task": task,
                "sms_count": sms_count,
                "via_app": via_app,
                "via_email": via_email,
                "via_sms": via_sms,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if template is not UNSET:
            field_dict["template"] = template
        if event is not UNSET:
            field_dict["event"] = event
        if state is not UNSET:
            field_dict["state"] = state
        if assignee_proximity is not UNSET:
            field_dict["assignee_proximity"] = assignee_proximity
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if emails is not UNSET:
            field_dict["emails"] = emails
        if phones is not UNSET:
            field_dict["phones"] = phones
        if message is not UNSET:
            field_dict["message"] = message
        if add_tracking_link is not UNSET:
            field_dict["add_tracking_link"] = add_tracking_link
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        method = d.pop("method")

        task = d.pop("task")

        sms_count = d.pop("sms_count")

        via_app = d.pop("via_app")

        via_email = d.pop("via_email")

        via_sms = d.pop("via_sms")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        template = d.pop("template", UNSET)

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

        def _parse_state(data: object) -> Union[BlankEnum, None, StateEf4Enum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _state_type_0 = data
                state_type_0: Union[Unset, StateEf4Enum]
                if isinstance(_state_type_0, Unset):
                    state_type_0 = UNSET
                else:
                    state_type_0 = StateEf4Enum(_state_type_0)

                return state_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _state_type_1 = data
                state_type_1: Union[Unset, BlankEnum]
                if isinstance(_state_type_1, Unset):
                    state_type_1 = UNSET
                else:
                    state_type_1 = BlankEnum(_state_type_1)

                return state_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, None, StateEf4Enum, Unset], data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_assignee_proximity(data: object) -> Union[AssigneeProximityEnum, BlankEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _assignee_proximity_type_0 = data
                assignee_proximity_type_0: Union[Unset, AssigneeProximityEnum]
                if isinstance(_assignee_proximity_type_0, Unset):
                    assignee_proximity_type_0 = UNSET
                else:
                    assignee_proximity_type_0 = AssigneeProximityEnum(_assignee_proximity_type_0)

                return assignee_proximity_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _assignee_proximity_type_1 = data
                assignee_proximity_type_1: Union[Unset, BlankEnum]
                if isinstance(_assignee_proximity_type_1, Unset):
                    assignee_proximity_type_1 = UNSET
                else:
                    assignee_proximity_type_1 = BlankEnum(_assignee_proximity_type_1)

                return assignee_proximity_type_1
            except:  # noqa: E722
                pass
            return cast(Union[AssigneeProximityEnum, BlankEnum, None, Unset], data)

        assignee_proximity = _parse_assignee_proximity(d.pop("assignee_proximity", UNSET))

        def _parse_recipient(data: object) -> Union[BlankEnum, None, RecipientEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _recipient_type_0 = data
                recipient_type_0: Union[Unset, RecipientEnum]
                if isinstance(_recipient_type_0, Unset):
                    recipient_type_0 = UNSET
                else:
                    recipient_type_0 = RecipientEnum(_recipient_type_0)

                return recipient_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _recipient_type_1 = data
                recipient_type_1: Union[Unset, BlankEnum]
                if isinstance(_recipient_type_1, Unset):
                    recipient_type_1 = UNSET
                else:
                    recipient_type_1 = BlankEnum(_recipient_type_1)

                return recipient_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, None, RecipientEnum, Unset], data)

        recipient = _parse_recipient(d.pop("recipient", UNSET))

        emails = cast(List[str], d.pop("emails", UNSET))

        phones = cast(List[str], d.pop("phones", UNSET))

        message = d.pop("message", UNSET)

        add_tracking_link = d.pop("add_tracking_link", UNSET)

        _sent_at = d.pop("sent_at", UNSET)
        sent_at: Union[Unset, None, datetime.datetime]
        if _sent_at is None:
            sent_at = None
        elif isinstance(_sent_at, Unset):
            sent_at = UNSET
        else:
            sent_at = isoparse(_sent_at)

        notification = cls(
            id=id,
            url=url,
            method=method,
            task=task,
            sms_count=sms_count,
            via_app=via_app,
            via_email=via_email,
            via_sms=via_sms,
            created_at=created_at,
            updated_at=updated_at,
            template=template,
            event=event,
            state=state,
            assignee_proximity=assignee_proximity,
            recipient=recipient,
            emails=emails,
            phones=phones,
            message=message,
            add_tracking_link=add_tracking_link,
            sent_at=sent_at,
        )

        notification.additional_properties = d
        return notification

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

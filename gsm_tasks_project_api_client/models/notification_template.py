import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.event_enum import EventEnum
from ..models.recipient_enum import RecipientEnum
from ..models.state_ef_4_enum import StateEf4Enum
from ..models.task_category_enum import TaskCategoryEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationTemplate")


@attr.s(auto_attribs=True)
class NotificationTemplate:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        name (str):
        message (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        event (Union[BlankEnum, EventEnum, Unset]):
        state (Union[BlankEnum, StateEf4Enum, Unset]):
        task_category (Union[BlankEnum, None, TaskCategoryEnum, Unset]):
        scheduled_time_change (Union[Unset, bool]):
        recipient (Union[BlankEnum, None, RecipientEnum, Unset]):
        via_sms (Union[Unset, bool]):
        via_email (Union[Unset, bool]):
        via_app (Union[Unset, bool]):
        is_active (Union[Unset, bool]):
        email_reply_to (Union[Unset, str]):
    """

    id: str
    url: str
    account: str
    name: str
    message: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    event: Union[BlankEnum, EventEnum, Unset] = UNSET
    state: Union[BlankEnum, StateEf4Enum, Unset] = UNSET
    task_category: Union[BlankEnum, None, TaskCategoryEnum, Unset] = UNSET
    scheduled_time_change: Union[Unset, bool] = UNSET
    recipient: Union[BlankEnum, None, RecipientEnum, Unset] = UNSET
    via_sms: Union[Unset, bool] = UNSET
    via_email: Union[Unset, bool] = UNSET
    via_app: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
    email_reply_to: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        name = self.name
        message = self.message
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        event: Union[Unset, str]
        if isinstance(self.event, Unset):
            event = UNSET

        elif isinstance(self.event, EventEnum):
            event = UNSET
            if not isinstance(self.event, Unset):
                event = self.event.value

        else:
            event = UNSET
            if not isinstance(self.event, Unset):
                event = self.event.value

        state: Union[Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET

        elif isinstance(self.state, StateEf4Enum):
            state = UNSET
            if not isinstance(self.state, Unset):
                state = self.state.value

        else:
            state = UNSET
            if not isinstance(self.state, Unset):
                state = self.state.value

        task_category: Union[None, Unset, str]
        if isinstance(self.task_category, Unset):
            task_category = UNSET
        elif self.task_category is None:
            task_category = None

        elif isinstance(self.task_category, TaskCategoryEnum):
            task_category = UNSET
            if not isinstance(self.task_category, Unset):
                task_category = self.task_category.value

        elif isinstance(self.task_category, BlankEnum):
            task_category = UNSET
            if not isinstance(self.task_category, Unset):
                task_category = self.task_category.value

        else:
            task_category = self.task_category

        scheduled_time_change = self.scheduled_time_change
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

        via_sms = self.via_sms
        via_email = self.via_email
        via_app = self.via_app
        is_active = self.is_active
        email_reply_to = self.email_reply_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "name": name,
                "message": message,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if event is not UNSET:
            field_dict["event"] = event
        if state is not UNSET:
            field_dict["state"] = state
        if task_category is not UNSET:
            field_dict["task_category"] = task_category
        if scheduled_time_change is not UNSET:
            field_dict["scheduled_time_change"] = scheduled_time_change
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if via_sms is not UNSET:
            field_dict["via_sms"] = via_sms
        if via_email is not UNSET:
            field_dict["via_email"] = via_email
        if via_app is not UNSET:
            field_dict["via_app"] = via_app
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if email_reply_to is not UNSET:
            field_dict["email_reply_to"] = email_reply_to

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        message = self.message if isinstance(self.message, Unset) else (None, str(self.message).encode(), "text/plain")
        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        event: Union[Unset, str]
        if isinstance(self.event, Unset):
            event = UNSET

        elif isinstance(self.event, EventEnum):
            event = UNSET
            if not isinstance(self.event, Unset):
                event = (None, str(self.event.value).encode(), "text/plain")

        else:
            event = UNSET
            if not isinstance(self.event, Unset):
                event = (None, str(self.event.value).encode(), "text/plain")

        state: Union[Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET

        elif isinstance(self.state, StateEf4Enum):
            state = UNSET
            if not isinstance(self.state, Unset):
                state = (None, str(self.state.value).encode(), "text/plain")

        else:
            state = UNSET
            if not isinstance(self.state, Unset):
                state = (None, str(self.state.value).encode(), "text/plain")

        task_category: Union[None, Unset, str]
        if isinstance(self.task_category, Unset):
            task_category = UNSET
        elif self.task_category is None:
            task_category = None

        elif isinstance(self.task_category, TaskCategoryEnum):
            task_category = UNSET
            if not isinstance(self.task_category, Unset):
                task_category = (None, str(self.task_category.value).encode(), "text/plain")

        elif isinstance(self.task_category, BlankEnum):
            task_category = UNSET
            if not isinstance(self.task_category, Unset):
                task_category = (None, str(self.task_category.value).encode(), "text/plain")

        else:
            task_category = self.task_category

        scheduled_time_change = (
            self.scheduled_time_change
            if isinstance(self.scheduled_time_change, Unset)
            else (None, str(self.scheduled_time_change).encode(), "text/plain")
        )
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

        via_sms = self.via_sms if isinstance(self.via_sms, Unset) else (None, str(self.via_sms).encode(), "text/plain")
        via_email = (
            self.via_email if isinstance(self.via_email, Unset) else (None, str(self.via_email).encode(), "text/plain")
        )
        via_app = self.via_app if isinstance(self.via_app, Unset) else (None, str(self.via_app).encode(), "text/plain")
        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )
        email_reply_to = (
            self.email_reply_to
            if isinstance(self.email_reply_to, Unset)
            else (None, str(self.email_reply_to).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "name": name,
                "message": message,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if event is not UNSET:
            field_dict["event"] = event
        if state is not UNSET:
            field_dict["state"] = state
        if task_category is not UNSET:
            field_dict["task_category"] = task_category
        if scheduled_time_change is not UNSET:
            field_dict["scheduled_time_change"] = scheduled_time_change
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if via_sms is not UNSET:
            field_dict["via_sms"] = via_sms
        if via_email is not UNSET:
            field_dict["via_email"] = via_email
        if via_app is not UNSET:
            field_dict["via_app"] = via_app
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if email_reply_to is not UNSET:
            field_dict["email_reply_to"] = email_reply_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        name = d.pop("name")

        message = d.pop("message")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_event(data: object) -> Union[BlankEnum, EventEnum, Unset]:
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
            if not isinstance(data, str):
                raise TypeError()
            _event_type_1 = data
            event_type_1: Union[Unset, BlankEnum]
            if isinstance(_event_type_1, Unset):
                event_type_1 = UNSET
            else:
                event_type_1 = BlankEnum(_event_type_1)

            return event_type_1

        event = _parse_event(d.pop("event", UNSET))

        def _parse_state(data: object) -> Union[BlankEnum, StateEf4Enum, Unset]:
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
            if not isinstance(data, str):
                raise TypeError()
            _state_type_1 = data
            state_type_1: Union[Unset, BlankEnum]
            if isinstance(_state_type_1, Unset):
                state_type_1 = UNSET
            else:
                state_type_1 = BlankEnum(_state_type_1)

            return state_type_1

        state = _parse_state(d.pop("state", UNSET))

        def _parse_task_category(data: object) -> Union[BlankEnum, None, TaskCategoryEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _task_category_type_0 = data
                task_category_type_0: Union[Unset, TaskCategoryEnum]
                if isinstance(_task_category_type_0, Unset):
                    task_category_type_0 = UNSET
                else:
                    task_category_type_0 = TaskCategoryEnum(_task_category_type_0)

                return task_category_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _task_category_type_1 = data
                task_category_type_1: Union[Unset, BlankEnum]
                if isinstance(_task_category_type_1, Unset):
                    task_category_type_1 = UNSET
                else:
                    task_category_type_1 = BlankEnum(_task_category_type_1)

                return task_category_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, None, TaskCategoryEnum, Unset], data)

        task_category = _parse_task_category(d.pop("task_category", UNSET))

        scheduled_time_change = d.pop("scheduled_time_change", UNSET)

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

        via_sms = d.pop("via_sms", UNSET)

        via_email = d.pop("via_email", UNSET)

        via_app = d.pop("via_app", UNSET)

        is_active = d.pop("is_active", UNSET)

        email_reply_to = d.pop("email_reply_to", UNSET)

        notification_template = cls(
            id=id,
            url=url,
            account=account,
            name=name,
            message=message,
            created_at=created_at,
            updated_at=updated_at,
            event=event,
            state=state,
            task_category=task_category,
            scheduled_time_change=scheduled_time_change,
            recipient=recipient,
            via_sms=via_sms,
            via_email=via_email,
            via_app=via_app,
            is_active=is_active,
            email_reply_to=email_reply_to,
        )

        notification_template.additional_properties = d
        return notification_template

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

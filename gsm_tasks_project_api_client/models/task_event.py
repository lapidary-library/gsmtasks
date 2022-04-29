import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.event_enum import EventEnum
from ..models.field_enum import FieldEnum
from ..models.from_state_enum import FromStateEnum
from ..models.task_event_location import TaskEventLocation
from ..models.to_state_enum import ToStateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskEvent")


@attr.s(auto_attribs=True)
class TaskEvent:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        task (str):
        task_command (str):
        field (Union[BlankEnum, FieldEnum]):
        event (EventEnum):
        from_state (FromStateEnum):
        to_state (ToStateEnum):
        user (str):
        assignee (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        notes (Union[Unset, str]): Event notes
        location (Union[Unset, None, TaskEventLocation]):
    """

    id: str
    url: str
    account: str
    task: str
    task_command: str
    field: Union[BlankEnum, FieldEnum]
    event: EventEnum
    from_state: FromStateEnum
    to_state: ToStateEnum
    user: str
    assignee: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    notes: Union[Unset, str] = UNSET
    location: Union[Unset, None, TaskEventLocation] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        task = self.task
        task_command = self.task_command

        if isinstance(self.field, FieldEnum):
            field = self.field.value

        else:
            field = self.field.value

        event = self.event.value

        from_state = self.from_state.value

        to_state = self.to_state.value

        user = self.user
        assignee = self.assignee
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        notes = self.notes
        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "task": task,
                "task_command": task_command,
                "field": field,
                "event": event,
                "from_state": from_state,
                "to_state": to_state,
                "user": user,
                "assignee": assignee,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        task = d.pop("task")

        task_command = d.pop("task_command")

        def _parse_field(data: object) -> Union[BlankEnum, FieldEnum]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                field_type_0 = FieldEnum(data)

                return field_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            field_type_1 = BlankEnum(data)

            return field_type_1

        field = _parse_field(d.pop("field"))

        event = EventEnum(d.pop("event"))

        from_state = FromStateEnum(d.pop("from_state"))

        to_state = ToStateEnum(d.pop("to_state"))

        user = d.pop("user")

        assignee = d.pop("assignee")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        notes = d.pop("notes", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, None, TaskEventLocation]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = TaskEventLocation.from_dict(_location)

        task_event = cls(
            id=id,
            url=url,
            account=account,
            task=task,
            task_command=task_command,
            field=field,
            event=event,
            from_state=from_state,
            to_state=to_state,
            user=user,
            assignee=assignee,
            created_at=created_at,
            updated_at=updated_at,
            notes=notes,
            location=location,
        )

        task_event.additional_properties = d
        return task_event

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

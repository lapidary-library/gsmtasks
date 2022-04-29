import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.event_enum import EventEnum
from ..models.from_state_enum import FromStateEnum
from ..models.to_state_enum import ToStateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskEventTrack")


@attr.s(auto_attribs=True)
class TaskEventTrack:
    """A subclass of ModelSerializer
    that outputs geojson-ready data as
    features and feature collections

        Attributes:
            id (str):
            model (str):
            url (str):
            task (str):
            task_event (str):
            event (EventEnum):
            from_state (FromStateEnum):
            to_state (ToStateEnum):
            user (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            track (str):
            notes (Union[Unset, str]): Event notes
            assignee (Union[Unset, None, str]):
    """

    id: str
    model: str
    url: str
    task: str
    task_event: str
    event: EventEnum
    from_state: FromStateEnum
    to_state: ToStateEnum
    user: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    track: str
    notes: Union[Unset, str] = UNSET
    assignee: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        model = self.model
        url = self.url
        task = self.task
        task_event = self.task_event
        event = self.event.value

        from_state = self.from_state.value

        to_state = self.to_state.value

        user = self.user
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        track = self.track
        notes = self.notes
        assignee = self.assignee

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "model": model,
                "url": url,
                "task": task,
                "task_event": task_event,
                "event": event,
                "from_state": from_state,
                "to_state": to_state,
                "user": user,
                "created_at": created_at,
                "updated_at": updated_at,
                "track": track,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes
        if assignee is not UNSET:
            field_dict["assignee"] = assignee

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        model = d.pop("model")

        url = d.pop("url")

        task = d.pop("task")

        task_event = d.pop("task_event")

        event = EventEnum(d.pop("event"))

        from_state = FromStateEnum(d.pop("from_state"))

        to_state = ToStateEnum(d.pop("to_state"))

        user = d.pop("user")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        track = d.pop("track")

        notes = d.pop("notes", UNSET)

        assignee = d.pop("assignee", UNSET)

        task_event_track = cls(
            id=id,
            model=model,
            url=url,
            task=task,
            task_event=task_event,
            event=event,
            from_state=from_state,
            to_state=to_state,
            user=user,
            created_at=created_at,
            updated_at=updated_at,
            track=track,
            notes=notes,
            assignee=assignee,
        )

        task_event_track.additional_properties = d
        return task_event_track

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

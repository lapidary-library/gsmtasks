from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.task_action_location import TaskActionLocation
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskAction")


@attr.s(auto_attribs=True)
class TaskAction:
    """
    Attributes:
        notes (Union[Unset, str]):
        location (Union[Unset, None, TaskActionLocation]):
    """

    notes: Union[Unset, str] = UNSET
    location: Union[Unset, None, TaskActionLocation] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notes = self.notes
        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notes is not UNSET:
            field_dict["notes"] = notes
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        notes = d.pop("notes", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, None, TaskActionLocation]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = TaskActionLocation.from_dict(_location)

        task_action = cls(
            notes=notes,
            location=location,
        )

        task_action.additional_properties = d
        return task_action

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

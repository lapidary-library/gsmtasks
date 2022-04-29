import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.task_command_task_data_metafields import TaskCommandTaskDataMetafields
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskCommandTaskData")


@attr.s(auto_attribs=True)
class TaskCommandTaskData:
    """
    Attributes:
        scheduled_time (Union[Unset, datetime.datetime]):
        position (Union[Unset, float]):
        metafields (Union[Unset, TaskCommandTaskDataMetafields]):
    """

    scheduled_time: Union[Unset, datetime.datetime] = UNSET
    position: Union[Unset, float] = UNSET
    metafields: Union[Unset, TaskCommandTaskDataMetafields] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scheduled_time: Union[Unset, str] = UNSET
        if not isinstance(self.scheduled_time, Unset):
            scheduled_time = self.scheduled_time.isoformat()

        position = self.position
        metafields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metafields, Unset):
            metafields = self.metafields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scheduled_time is not UNSET:
            field_dict["scheduled_time"] = scheduled_time
        if position is not UNSET:
            field_dict["position"] = position
        if metafields is not UNSET:
            field_dict["metafields"] = metafields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _scheduled_time = d.pop("scheduled_time", UNSET)
        scheduled_time: Union[Unset, datetime.datetime]
        if isinstance(_scheduled_time, Unset):
            scheduled_time = UNSET
        else:
            scheduled_time = isoparse(_scheduled_time)

        position = d.pop("position", UNSET)

        _metafields = d.pop("metafields", UNSET)
        metafields: Union[Unset, TaskCommandTaskDataMetafields]
        if isinstance(_metafields, Unset):
            metafields = UNSET
        else:
            metafields = TaskCommandTaskDataMetafields.from_dict(_metafields)

        task_command_task_data = cls(
            scheduled_time=scheduled_time,
            position=position,
            metafields=metafields,
        )

        task_command_task_data.additional_properties = d
        return task_command_task_data

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

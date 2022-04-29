from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.category_enum import CategoryEnum
from ..models.state_ef_4_enum import StateEf4Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskAddressFeature")


@attr.s(auto_attribs=True)
class TaskAddressFeature:
    """A subclass of ModelSerializer
    that outputs geojson-ready data as
    features and feature collections

        Attributes:
            model (str):
            id (str):
            task (str):
            formatted_address (str):
            geometry (str):
            category (Union[Unset, CategoryEnum]):
            state (Union[Unset, StateEf4Enum]):
    """

    model: str
    id: str
    task: str
    formatted_address: str
    geometry: str
    category: Union[Unset, CategoryEnum] = UNSET
    state: Union[Unset, StateEf4Enum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model = self.model
        id = self.id
        task = self.task
        formatted_address = self.formatted_address
        geometry = self.geometry
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "id": id,
                "task": task,
                "formatted_address": formatted_address,
                "geometry": geometry,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        model = d.pop("model")

        id = d.pop("id")

        task = d.pop("task")

        formatted_address = d.pop("formatted_address")

        geometry = d.pop("geometry")

        _category = d.pop("category", UNSET)
        category: Union[Unset, CategoryEnum]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CategoryEnum(_category)

        _state = d.pop("state", UNSET)
        state: Union[Unset, StateEf4Enum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = StateEf4Enum(_state)

        task_address_feature = cls(
            model=model,
            id=id,
            task=task,
            formatted_address=formatted_address,
            geometry=geometry,
            category=category,
            state=state,
        )

        task_address_feature.additional_properties = d
        return task_address_feature

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

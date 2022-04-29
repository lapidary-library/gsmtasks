from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import Unset

T = TypeVar("T", bound="RenderRequest")


@attr.s(auto_attribs=True)
class RenderRequest:
    """
    Attributes:
        task (str):
    """

    task: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        task = self.task

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task": task,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        task = self.task if isinstance(self.task, Unset) else (None, str(self.task).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "task": task,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        task = d.pop("task")

        render_request = cls(
            task=task,
        )

        render_request.additional_properties = d
        return render_request

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

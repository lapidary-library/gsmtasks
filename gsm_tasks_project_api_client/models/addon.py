from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Addon")


@attr.s(auto_attribs=True)
class Addon:
    """
    Attributes:
        id (str):
        name (str):
        short_description (str):
        description (str):
        price (str):
    """

    id: str
    name: str
    short_description: str
    description: str
    price: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        short_description = self.short_description
        description = self.description
        price = self.price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "short_description": short_description,
                "description": description,
                "price": price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        short_description = d.pop("short_description")

        description = d.pop("description")

        price = d.pop("price")

        addon = cls(
            id=id,
            name=name,
            short_description=short_description,
            description=description,
            price=price,
        )

        addon.additional_properties = d
        return addon

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

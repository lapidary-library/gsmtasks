from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PublicUser")


@attr.s(auto_attribs=True)
class PublicUser:
    """
    Attributes:
        id (str):
        url (str):
        display_name (str):
        email (str):
    """

    id: str
    url: str
    display_name: str
    email: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        display_name = self.display_name
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_name": display_name,
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        display_name = d.pop("display_name")

        email = d.pop("email")

        public_user = cls(
            id=id,
            url=url,
            display_name=display_name,
            email=email,
        )

        public_user.additional_properties = d
        return public_user

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

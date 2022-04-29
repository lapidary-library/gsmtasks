from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegistrationUser")


@attr.s(auto_attribs=True)
class RegistrationUser:
    """
    Attributes:
        id (str):
        url (str):
        name (str):
        email (str):
        password (str):
        phone (Union[Unset, str]):
    """

    id: str
    url: str
    name: str
    email: str
    password: str
    phone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        name = self.name
        email = self.email
        password = self.password
        phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "name": name,
                "email": email,
                "password": password,
            }
        )
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        name = d.pop("name")

        email = d.pop("email")

        password = d.pop("password")

        phone = d.pop("phone", UNSET)

        registration_user = cls(
            id=id,
            url=url,
            name=name,
            email=email,
            password=password,
            phone=phone,
        )

        registration_user.additional_properties = d
        return registration_user

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

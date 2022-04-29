from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import Unset

T = TypeVar("T", bound="AccountUser")


@attr.s(auto_attribs=True)
class AccountUser:
    """
    Attributes:
        id (str):
        url (str):
        first_name (str):
        last_name (str):
        display_name (str):
        email (str):
        phone (str):
        is_on_duty (str):
    """

    id: str
    url: str
    first_name: str
    last_name: str
    display_name: str
    email: str
    phone: str
    is_on_duty: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        first_name = self.first_name
        last_name = self.last_name
        display_name = self.display_name
        email = self.email
        phone = self.phone
        is_on_duty = self.is_on_duty

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "first_name": first_name,
                "last_name": last_name,
                "display_name": display_name,
                "email": email,
                "phone": phone,
                "is_on_duty": is_on_duty,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        first_name = (
            self.first_name
            if isinstance(self.first_name, Unset)
            else (None, str(self.first_name).encode(), "text/plain")
        )
        last_name = (
            self.last_name if isinstance(self.last_name, Unset) else (None, str(self.last_name).encode(), "text/plain")
        )
        display_name = (
            self.display_name
            if isinstance(self.display_name, Unset)
            else (None, str(self.display_name).encode(), "text/plain")
        )
        email = self.email if isinstance(self.email, Unset) else (None, str(self.email).encode(), "text/plain")
        phone = self.phone if isinstance(self.phone, Unset) else (None, str(self.phone).encode(), "text/plain")
        is_on_duty = (
            self.is_on_duty
            if isinstance(self.is_on_duty, Unset)
            else (None, str(self.is_on_duty).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "first_name": first_name,
                "last_name": last_name,
                "display_name": display_name,
                "email": email,
                "phone": phone,
                "is_on_duty": is_on_duty,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        display_name = d.pop("display_name")

        email = d.pop("email")

        phone = d.pop("phone")

        is_on_duty = d.pop("is_on_duty")

        account_user = cls(
            id=id,
            url=url,
            first_name=first_name,
            last_name=last_name,
            display_name=display_name,
            email=email,
            phone=phone,
            is_on_duty=is_on_duty,
        )

        account_user.additional_properties = d
        return account_user

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

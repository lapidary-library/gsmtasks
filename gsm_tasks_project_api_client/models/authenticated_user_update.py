from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.nested_address import NestedAddress
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticatedUserUpdate")


@attr.s(auto_attribs=True)
class AuthenticatedUserUpdate:
    """
    Attributes:
        id (str):
        url (str):
        display_name (str):
        email (str):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        phone (Union[Unset, str]):
        address (Union[Unset, NestedAddress]):
    """

    id: str
    url: str
    display_name: str
    email: str
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    address: Union[Unset, NestedAddress] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        display_name = self.display_name
        email = self.email
        first_name = self.first_name
        last_name = self.last_name
        phone = self.phone
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

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
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        display_name = d.pop("display_name")

        email = d.pop("email")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        phone = d.pop("phone", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, NestedAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = NestedAddress.from_dict(_address)

        authenticated_user_update = cls(
            id=id,
            url=url,
            display_name=display_name,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
        )

        authenticated_user_update.additional_properties = d
        return authenticated_user_update

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

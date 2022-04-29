from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReadableUser")


@attr.s(auto_attribs=True)
class ReadableUser:
    """
    Attributes:
        id (str):
        url (str):
        display_name (str):
        email (str):
        intercom_hash (str):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        phone (Union[Unset, str]):
        signature_image (Union[Unset, str]):
    """

    id: str
    url: str
    display_name: str
    email: str
    intercom_hash: str
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    signature_image: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        display_name = self.display_name
        email = self.email
        intercom_hash = self.intercom_hash
        first_name = self.first_name
        last_name = self.last_name
        phone = self.phone
        signature_image = self.signature_image

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_name": display_name,
                "email": email,
                "intercom_hash": intercom_hash,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if signature_image is not UNSET:
            field_dict["signature_image"] = signature_image

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        display_name = d.pop("display_name")

        email = d.pop("email")

        intercom_hash = d.pop("intercom_hash")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        phone = d.pop("phone", UNSET)

        signature_image = d.pop("signature_image", UNSET)

        readable_user = cls(
            id=id,
            url=url,
            display_name=display_name,
            email=email,
            intercom_hash=intercom_hash,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            signature_image=signature_image,
        )

        readable_user.additional_properties = d
        return readable_user

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

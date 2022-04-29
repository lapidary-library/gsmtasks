from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LegacyNestedContact")


@attr.s(auto_attribs=True)
class LegacyNestedContact:
    """Support depreciated fields phone and email

    write to new fields phones[0] and emails[0]

        Attributes:
            name (Union[Unset, str]):
            company (Union[Unset, str]):
            phone (Union[Unset, None, str]):
            email (Union[Unset, None, str]):
            phones (Union[Unset, List[str]]):
            emails (Union[Unset, List[str]]):
            notes (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    company: Union[Unset, str] = UNSET
    phone: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    phones: Union[Unset, List[str]] = UNSET
    emails: Union[Unset, List[str]] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        company = self.company
        phone = self.phone
        email = self.email
        phones: Union[Unset, List[str]] = UNSET
        if not isinstance(self.phones, Unset):
            phones = self.phones

        emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        notes = self.notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if company is not UNSET:
            field_dict["company"] = company
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if phones is not UNSET:
            field_dict["phones"] = phones
        if emails is not UNSET:
            field_dict["emails"] = emails
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        company = d.pop("company", UNSET)

        phone = d.pop("phone", UNSET)

        email = d.pop("email", UNSET)

        phones = cast(List[str], d.pop("phones", UNSET))

        emails = cast(List[str], d.pop("emails", UNSET))

        notes = d.pop("notes", UNSET)

        legacy_nested_contact = cls(
            name=name,
            company=company,
            phone=phone,
            email=email,
            phones=phones,
            emails=emails,
            notes=notes,
        )

        legacy_nested_contact.additional_properties = d
        return legacy_nested_contact

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

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.blank_enum import BlankEnum
from ..models.timezone_enum import TimezoneEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="RegistrationAccount")


@attr.s(auto_attribs=True)
class RegistrationAccount:
    """
    Attributes:
        id (str):
        url (str):
        name (str):
        timezone (Union[BlankEnum, None, TimezoneEnum, Unset]):
        country_code (Union[Unset, str]):
    """

    id: str
    url: str
    name: str
    timezone: Union[BlankEnum, None, TimezoneEnum, Unset] = UNSET
    country_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        name = self.name
        timezone: Union[None, Unset, str]
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        elif self.timezone is None:
            timezone = None

        elif isinstance(self.timezone, TimezoneEnum):
            timezone = UNSET
            if not isinstance(self.timezone, Unset):
                timezone = self.timezone.value

        elif isinstance(self.timezone, BlankEnum):
            timezone = UNSET
            if not isinstance(self.timezone, Unset):
                timezone = self.timezone.value

        else:
            timezone = self.timezone

        country_code = self.country_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "name": name,
            }
        )
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if country_code is not UNSET:
            field_dict["country_code"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        name = d.pop("name")

        def _parse_timezone(data: object) -> Union[BlankEnum, None, TimezoneEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _timezone_type_0 = data
                timezone_type_0: Union[Unset, TimezoneEnum]
                if isinstance(_timezone_type_0, Unset):
                    timezone_type_0 = UNSET
                else:
                    timezone_type_0 = TimezoneEnum(_timezone_type_0)

                return timezone_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _timezone_type_1 = data
                timezone_type_1: Union[Unset, BlankEnum]
                if isinstance(_timezone_type_1, Unset):
                    timezone_type_1 = UNSET
                else:
                    timezone_type_1 = BlankEnum(_timezone_type_1)

                return timezone_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, None, TimezoneEnum, Unset], data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        country_code = d.pop("country_code", UNSET)

        registration_account = cls(
            id=id,
            url=url,
            name=name,
            timezone=timezone,
            country_code=country_code,
        )

        registration_account.additional_properties = d
        return registration_account

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

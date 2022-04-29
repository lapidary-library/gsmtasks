from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.nested_address_location import NestedAddressLocation
from ..types import UNSET, Unset

T = TypeVar("T", bound="NestedAddress")


@attr.s(auto_attribs=True)
class NestedAddress:
    """
    Attributes:
        raw_address (Union[Unset, str]):
        formatted_address (Union[Unset, str]):
        location (Union[Unset, None, NestedAddressLocation]):
        google_place_id (Union[Unset, str]):
        point_of_interest (Union[Unset, str]):
        street (Union[Unset, str]):
        house_number (Union[Unset, str]):
        apartment_number (Union[Unset, None, str]):
        city (Union[Unset, str]):
        state (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        country (Union[Unset, str]):
        country_code (Union[Unset, str]):
    """

    raw_address: Union[Unset, str] = UNSET
    formatted_address: Union[Unset, str] = UNSET
    location: Union[Unset, None, NestedAddressLocation] = UNSET
    google_place_id: Union[Unset, str] = UNSET
    point_of_interest: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    house_number: Union[Unset, str] = UNSET
    apartment_number: Union[Unset, None, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        raw_address = self.raw_address
        formatted_address = self.formatted_address
        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        google_place_id = self.google_place_id
        point_of_interest = self.point_of_interest
        street = self.street
        house_number = self.house_number
        apartment_number = self.apartment_number
        city = self.city
        state = self.state
        postal_code = self.postal_code
        country = self.country
        country_code = self.country_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if raw_address is not UNSET:
            field_dict["raw_address"] = raw_address
        if formatted_address is not UNSET:
            field_dict["formatted_address"] = formatted_address
        if location is not UNSET:
            field_dict["location"] = location
        if google_place_id is not UNSET:
            field_dict["google_place_id"] = google_place_id
        if point_of_interest is not UNSET:
            field_dict["point_of_interest"] = point_of_interest
        if street is not UNSET:
            field_dict["street"] = street
        if house_number is not UNSET:
            field_dict["house_number"] = house_number
        if apartment_number is not UNSET:
            field_dict["apartment_number"] = apartment_number
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["country_code"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        raw_address = d.pop("raw_address", UNSET)

        formatted_address = d.pop("formatted_address", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, None, NestedAddressLocation]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = NestedAddressLocation.from_dict(_location)

        google_place_id = d.pop("google_place_id", UNSET)

        point_of_interest = d.pop("point_of_interest", UNSET)

        street = d.pop("street", UNSET)

        house_number = d.pop("house_number", UNSET)

        apartment_number = d.pop("apartment_number", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        country = d.pop("country", UNSET)

        country_code = d.pop("country_code", UNSET)

        nested_address = cls(
            raw_address=raw_address,
            formatted_address=formatted_address,
            location=location,
            google_place_id=google_place_id,
            point_of_interest=point_of_interest,
            street=street,
            house_number=house_number,
            apartment_number=apartment_number,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            country_code=country_code,
        )

        nested_address.additional_properties = d
        return nested_address

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

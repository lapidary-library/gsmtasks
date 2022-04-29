import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.contact_address_export_address_location import ContactAddressExportAddressLocation
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactAddressExport")


@attr.s(auto_attribs=True)
class ContactAddressExport:
    """
    Attributes:
        id (str):
        address_location (ContactAddressExportAddressLocation):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        external_id (Union[Unset, None, str]):
        account_name (Union[Unset, str]):  Default: ''.
        contact_name (Union[Unset, str]):  Default: ''.
        contact_company (Union[Unset, str]):  Default: ''.
        contact_phones (Union[Unset, List[str]]):
        contact_emails (Union[Unset, List[str]]):
        contact_notes (Union[Unset, str]):  Default: ''.
        address_raw_address (Union[Unset, str]):  Default: ''.
        address_formatted_address (Union[Unset, str]):  Default: ''.
        address_google_place_id (Union[Unset, str]):  Default: ''.
        address_point_of_interest (Union[Unset, str]):  Default: ''.
        address_street (Union[Unset, str]):  Default: ''.
        address_house_number (Union[Unset, str]):  Default: ''.
        address_apartment_number (Union[Unset, str]):  Default: ''.
        address_city (Union[Unset, str]):  Default: ''.
        address_state (Union[Unset, str]):  Default: ''.
        address_postal_code (Union[Unset, str]):  Default: ''.
        address_country (Union[Unset, str]):  Default: ''.
        address_country_code (Union[Unset, str]):  Default: ''.
        is_orderer (Union[Unset, bool]):
        is_receiver (Union[Unset, bool]):
        source (Union[Unset, str]):
    """

    id: str
    address_location: ContactAddressExportAddressLocation
    created_at: datetime.datetime
    updated_at: datetime.datetime
    external_id: Union[Unset, None, str] = UNSET
    account_name: Union[Unset, str] = ""
    contact_name: Union[Unset, str] = ""
    contact_company: Union[Unset, str] = ""
    contact_phones: Union[Unset, List[str]] = UNSET
    contact_emails: Union[Unset, List[str]] = UNSET
    contact_notes: Union[Unset, str] = ""
    address_raw_address: Union[Unset, str] = ""
    address_formatted_address: Union[Unset, str] = ""
    address_google_place_id: Union[Unset, str] = ""
    address_point_of_interest: Union[Unset, str] = ""
    address_street: Union[Unset, str] = ""
    address_house_number: Union[Unset, str] = ""
    address_apartment_number: Union[Unset, str] = ""
    address_city: Union[Unset, str] = ""
    address_state: Union[Unset, str] = ""
    address_postal_code: Union[Unset, str] = ""
    address_country: Union[Unset, str] = ""
    address_country_code: Union[Unset, str] = ""
    is_orderer: Union[Unset, bool] = UNSET
    is_receiver: Union[Unset, bool] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        address_location = self.address_location.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        external_id = self.external_id
        account_name = self.account_name
        contact_name = self.contact_name
        contact_company = self.contact_company
        contact_phones: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contact_phones, Unset):
            contact_phones = self.contact_phones

        contact_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contact_emails, Unset):
            contact_emails = self.contact_emails

        contact_notes = self.contact_notes
        address_raw_address = self.address_raw_address
        address_formatted_address = self.address_formatted_address
        address_google_place_id = self.address_google_place_id
        address_point_of_interest = self.address_point_of_interest
        address_street = self.address_street
        address_house_number = self.address_house_number
        address_apartment_number = self.address_apartment_number
        address_city = self.address_city
        address_state = self.address_state
        address_postal_code = self.address_postal_code
        address_country = self.address_country
        address_country_code = self.address_country_code
        is_orderer = self.is_orderer
        is_receiver = self.is_receiver
        source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "address__location": address_location,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if account_name is not UNSET:
            field_dict["account__name"] = account_name
        if contact_name is not UNSET:
            field_dict["contact__name"] = contact_name
        if contact_company is not UNSET:
            field_dict["contact__company"] = contact_company
        if contact_phones is not UNSET:
            field_dict["contact__phones"] = contact_phones
        if contact_emails is not UNSET:
            field_dict["contact__emails"] = contact_emails
        if contact_notes is not UNSET:
            field_dict["contact__notes"] = contact_notes
        if address_raw_address is not UNSET:
            field_dict["address__raw_address"] = address_raw_address
        if address_formatted_address is not UNSET:
            field_dict["address__formatted_address"] = address_formatted_address
        if address_google_place_id is not UNSET:
            field_dict["address__google_place_id"] = address_google_place_id
        if address_point_of_interest is not UNSET:
            field_dict["address__point_of_interest"] = address_point_of_interest
        if address_street is not UNSET:
            field_dict["address__street"] = address_street
        if address_house_number is not UNSET:
            field_dict["address__house_number"] = address_house_number
        if address_apartment_number is not UNSET:
            field_dict["address__apartment_number"] = address_apartment_number
        if address_city is not UNSET:
            field_dict["address__city"] = address_city
        if address_state is not UNSET:
            field_dict["address__state"] = address_state
        if address_postal_code is not UNSET:
            field_dict["address__postal_code"] = address_postal_code
        if address_country is not UNSET:
            field_dict["address__country"] = address_country
        if address_country_code is not UNSET:
            field_dict["address__country_code"] = address_country_code
        if is_orderer is not UNSET:
            field_dict["is_orderer"] = is_orderer
        if is_receiver is not UNSET:
            field_dict["is_receiver"] = is_receiver
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        address_location = ContactAddressExportAddressLocation.from_dict(d.pop("address__location"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        external_id = d.pop("external_id", UNSET)

        account_name = d.pop("account__name", UNSET)

        contact_name = d.pop("contact__name", UNSET)

        contact_company = d.pop("contact__company", UNSET)

        contact_phones = cast(List[str], d.pop("contact__phones", UNSET))

        contact_emails = cast(List[str], d.pop("contact__emails", UNSET))

        contact_notes = d.pop("contact__notes", UNSET)

        address_raw_address = d.pop("address__raw_address", UNSET)

        address_formatted_address = d.pop("address__formatted_address", UNSET)

        address_google_place_id = d.pop("address__google_place_id", UNSET)

        address_point_of_interest = d.pop("address__point_of_interest", UNSET)

        address_street = d.pop("address__street", UNSET)

        address_house_number = d.pop("address__house_number", UNSET)

        address_apartment_number = d.pop("address__apartment_number", UNSET)

        address_city = d.pop("address__city", UNSET)

        address_state = d.pop("address__state", UNSET)

        address_postal_code = d.pop("address__postal_code", UNSET)

        address_country = d.pop("address__country", UNSET)

        address_country_code = d.pop("address__country_code", UNSET)

        is_orderer = d.pop("is_orderer", UNSET)

        is_receiver = d.pop("is_receiver", UNSET)

        source = d.pop("source", UNSET)

        contact_address_export = cls(
            id=id,
            address_location=address_location,
            created_at=created_at,
            updated_at=updated_at,
            external_id=external_id,
            account_name=account_name,
            contact_name=contact_name,
            contact_company=contact_company,
            contact_phones=contact_phones,
            contact_emails=contact_emails,
            contact_notes=contact_notes,
            address_raw_address=address_raw_address,
            address_formatted_address=address_formatted_address,
            address_google_place_id=address_google_place_id,
            address_point_of_interest=address_point_of_interest,
            address_street=address_street,
            address_house_number=address_house_number,
            address_apartment_number=address_apartment_number,
            address_city=address_city,
            address_state=address_state,
            address_postal_code=address_postal_code,
            address_country=address_country,
            address_country_code=address_country_code,
            is_orderer=is_orderer,
            is_receiver=is_receiver,
            source=source,
        )

        contact_address_export.additional_properties = d
        return contact_address_export

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

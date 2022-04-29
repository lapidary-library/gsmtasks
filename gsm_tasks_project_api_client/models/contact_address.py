import datetime
import json
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.nested_address import NestedAddress
from ..models.nested_contact import NestedContact
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactAddress")


@attr.s(auto_attribs=True)
class ContactAddress:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        contact (NestedContact):
        address (NestedAddress):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        external_id (Union[Unset, None, str]):
        client (Union[Unset, str]):
        is_orderer (Union[Unset, bool]):
        is_receiver (Union[Unset, bool]):
        source (Union[Unset, str]):
    """

    id: str
    url: str
    account: str
    contact: NestedContact
    address: NestedAddress
    created_at: datetime.datetime
    updated_at: datetime.datetime
    external_id: Union[Unset, None, str] = UNSET
    client: Union[Unset, str] = UNSET
    is_orderer: Union[Unset, bool] = UNSET
    is_receiver: Union[Unset, bool] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        contact = self.contact.to_dict()

        address = self.address.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        external_id = self.external_id
        client = self.client
        is_orderer = self.is_orderer
        is_receiver = self.is_receiver
        source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "contact": contact,
                "address": address,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if client is not UNSET:
            field_dict["client"] = client
        if is_orderer is not UNSET:
            field_dict["is_orderer"] = is_orderer
        if is_receiver is not UNSET:
            field_dict["is_receiver"] = is_receiver
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        contact = (None, json.dumps(self.contact.to_dict()).encode(), "application/json")

        address = (None, json.dumps(self.address.to_dict()).encode(), "application/json")

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        external_id = (
            self.external_id
            if isinstance(self.external_id, Unset)
            else (None, str(self.external_id).encode(), "text/plain")
        )
        client = self.client if isinstance(self.client, Unset) else (None, str(self.client).encode(), "text/plain")
        is_orderer = (
            self.is_orderer
            if isinstance(self.is_orderer, Unset)
            else (None, str(self.is_orderer).encode(), "text/plain")
        )
        is_receiver = (
            self.is_receiver
            if isinstance(self.is_receiver, Unset)
            else (None, str(self.is_receiver).encode(), "text/plain")
        )
        source = self.source if isinstance(self.source, Unset) else (None, str(self.source).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "contact": contact,
                "address": address,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if client is not UNSET:
            field_dict["client"] = client
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

        url = d.pop("url")

        account = d.pop("account")

        contact = NestedContact.from_dict(d.pop("contact"))

        address = NestedAddress.from_dict(d.pop("address"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        external_id = d.pop("external_id", UNSET)

        client = d.pop("client", UNSET)

        is_orderer = d.pop("is_orderer", UNSET)

        is_receiver = d.pop("is_receiver", UNSET)

        source = d.pop("source", UNSET)

        contact_address = cls(
            id=id,
            url=url,
            account=account,
            contact=contact,
            address=address,
            created_at=created_at,
            updated_at=updated_at,
            external_id=external_id,
            client=client,
            is_orderer=is_orderer,
            is_receiver=is_receiver,
            source=source,
        )

        contact_address.additional_properties = d
        return contact_address

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

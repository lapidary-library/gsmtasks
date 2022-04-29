import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.nested_address import NestedAddress
from ..models.nested_contact import NestedContact
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedContactAddress")


@attr.s(auto_attribs=True)
class PatchedContactAddress:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        external_id (Union[Unset, None, str]):
        account (Union[Unset, str]):
        client (Union[Unset, str]):
        contact (Union[Unset, NestedContact]):
        address (Union[Unset, NestedAddress]):
        is_orderer (Union[Unset, bool]):
        is_receiver (Union[Unset, bool]):
        source (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    account: Union[Unset, str] = UNSET
    client: Union[Unset, str] = UNSET
    contact: Union[Unset, NestedContact] = UNSET
    address: Union[Unset, NestedAddress] = UNSET
    is_orderer: Union[Unset, bool] = UNSET
    is_receiver: Union[Unset, bool] = UNSET
    source: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        external_id = self.external_id
        account = self.account
        client = self.client
        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        is_orderer = self.is_orderer
        is_receiver = self.is_receiver
        source = self.source
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if account is not UNSET:
            field_dict["account"] = account
        if client is not UNSET:
            field_dict["client"] = client
        if contact is not UNSET:
            field_dict["contact"] = contact
        if address is not UNSET:
            field_dict["address"] = address
        if is_orderer is not UNSET:
            field_dict["is_orderer"] = is_orderer
        if is_receiver is not UNSET:
            field_dict["is_receiver"] = is_receiver
        if source is not UNSET:
            field_dict["source"] = source
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        external_id = (
            self.external_id
            if isinstance(self.external_id, Unset)
            else (None, str(self.external_id).encode(), "text/plain")
        )
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        client = self.client if isinstance(self.client, Unset) else (None, str(self.client).encode(), "text/plain")
        contact: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = (None, json.dumps(self.contact.to_dict()).encode(), "application/json")

        address: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.address, Unset):
            address = (None, json.dumps(self.address.to_dict()).encode(), "application/json")

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
        created_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        updated_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if account is not UNSET:
            field_dict["account"] = account
        if client is not UNSET:
            field_dict["client"] = client
        if contact is not UNSET:
            field_dict["contact"] = contact
        if address is not UNSET:
            field_dict["address"] = address
        if is_orderer is not UNSET:
            field_dict["is_orderer"] = is_orderer
        if is_receiver is not UNSET:
            field_dict["is_receiver"] = is_receiver
        if source is not UNSET:
            field_dict["source"] = source
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        external_id = d.pop("external_id", UNSET)

        account = d.pop("account", UNSET)

        client = d.pop("client", UNSET)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, NestedContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = NestedContact.from_dict(_contact)

        _address = d.pop("address", UNSET)
        address: Union[Unset, NestedAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = NestedAddress.from_dict(_address)

        is_orderer = d.pop("is_orderer", UNSET)

        is_receiver = d.pop("is_receiver", UNSET)

        source = d.pop("source", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        patched_contact_address = cls(
            id=id,
            url=url,
            external_id=external_id,
            account=account,
            client=client,
            contact=contact,
            address=address,
            is_orderer=is_orderer,
            is_receiver=is_receiver,
            source=source,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_contact_address.additional_properties = d
        return patched_contact_address

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

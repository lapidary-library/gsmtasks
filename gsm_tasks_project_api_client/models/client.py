import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Client")


@attr.s(auto_attribs=True)
class Client:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        name (str):
        slug (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        contact_addresses (str):
        archived (Union[Unset, bool]):
    """

    id: str
    url: str
    account: str
    name: str
    slug: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    contact_addresses: str
    archived: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        name = self.name
        slug = self.slug
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        contact_addresses = self.contact_addresses
        archived = self.archived

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "name": name,
                "slug": slug,
                "created_at": created_at,
                "updated_at": updated_at,
                "contact_addresses": contact_addresses,
            }
        )
        if archived is not UNSET:
            field_dict["archived"] = archived

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        slug = self.slug if isinstance(self.slug, Unset) else (None, str(self.slug).encode(), "text/plain")
        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        contact_addresses = (
            self.contact_addresses
            if isinstance(self.contact_addresses, Unset)
            else (None, str(self.contact_addresses).encode(), "text/plain")
        )
        archived = (
            self.archived if isinstance(self.archived, Unset) else (None, str(self.archived).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "name": name,
                "slug": slug,
                "created_at": created_at,
                "updated_at": updated_at,
                "contact_addresses": contact_addresses,
            }
        )
        if archived is not UNSET:
            field_dict["archived"] = archived

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        name = d.pop("name")

        slug = d.pop("slug")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        contact_addresses = d.pop("contact_addresses")

        archived = d.pop("archived", UNSET)

        client = cls(
            id=id,
            url=url,
            account=account,
            name=name,
            slug=slug,
            created_at=created_at,
            updated_at=updated_at,
            contact_addresses=contact_addresses,
            archived=archived,
        )

        client.additional_properties = d
        return client

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

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientRole")


@attr.s(auto_attribs=True)
class ClientRole:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        client (str):
        user (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        phone (Union[Unset, str]):
        is_manager (Union[Unset, bool]):
        is_active (Union[Unset, bool]): Designates whether this Client Role should be treated as active.
    """

    id: str
    url: str
    account: str
    client: str
    user: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    phone: Union[Unset, str] = UNSET
    is_manager: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        client = self.client
        user = self.user
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        phone = self.phone
        is_manager = self.is_manager
        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "client": client,
                "user": user,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if phone is not UNSET:
            field_dict["phone"] = phone
        if is_manager is not UNSET:
            field_dict["is_manager"] = is_manager
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        client = self.client if isinstance(self.client, Unset) else (None, str(self.client).encode(), "text/plain")
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        phone = self.phone if isinstance(self.phone, Unset) else (None, str(self.phone).encode(), "text/plain")
        is_manager = (
            self.is_manager
            if isinstance(self.is_manager, Unset)
            else (None, str(self.is_manager).encode(), "text/plain")
        )
        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
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
                "client": client,
                "user": user,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if phone is not UNSET:
            field_dict["phone"] = phone
        if is_manager is not UNSET:
            field_dict["is_manager"] = is_manager
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        client = d.pop("client")

        user = d.pop("user")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        phone = d.pop("phone", UNSET)

        is_manager = d.pop("is_manager", UNSET)

        is_active = d.pop("is_active", UNSET)

        client_role = cls(
            id=id,
            url=url,
            account=account,
            client=client,
            user=user,
            created_at=created_at,
            updated_at=updated_at,
            phone=phone,
            is_manager=is_manager,
            is_active=is_active,
        )

        client_role.additional_properties = d
        return client_role

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

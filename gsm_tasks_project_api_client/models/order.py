import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Order")


@attr.s(auto_attribs=True)
class Order:
    """
    Attributes:
        url (str):
        account (str):
        tasks (List[str]):
        created_by (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        id (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        reference (Union[Unset, str]):
        client (Union[Unset, None, str]):
        auto_assign (Union[Unset, bool]):
    """

    url: str
    account: str
    tasks: List[str]
    created_by: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    id: Union[Unset, None, str] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    reference: Union[Unset, str] = UNSET
    client: Union[Unset, None, str] = UNSET
    auto_assign: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        account = self.account
        tasks = self.tasks

        created_by = self.created_by
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        id = self.id
        external_id = self.external_id
        reference = self.reference
        client = self.client
        auto_assign = self.auto_assign

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "account": account,
                "tasks": tasks,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if client is not UNSET:
            field_dict["client"] = client
        if auto_assign is not UNSET:
            field_dict["auto_assign"] = auto_assign

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        account = d.pop("account")

        tasks = cast(List[str], d.pop("tasks"))

        created_by = d.pop("created_by")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        id = d.pop("id", UNSET)

        external_id = d.pop("external_id", UNSET)

        reference = d.pop("reference", UNSET)

        client = d.pop("client", UNSET)

        auto_assign = d.pop("auto_assign", UNSET)

        order = cls(
            url=url,
            account=account,
            tasks=tasks,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            external_id=external_id,
            reference=reference,
            client=client,
            auto_assign=auto_assign,
        )

        order.additional_properties = d
        return order

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

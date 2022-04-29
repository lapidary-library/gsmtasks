from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IntegrationRequest")


@attr.s(auto_attribs=True)
class IntegrationRequest:
    """
    Attributes:
        id (str):
        account (str):
        name (str):
        user (str):
        notes (Union[Unset, str]):
    """

    id: str
    account: str
    name: str
    user: str
    notes: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        account = self.account
        name = self.name
        user = self.user
        notes = self.notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "account": account,
                "name": name,
                "user": user,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        notes = self.notes if isinstance(self.notes, Unset) else (None, str(self.notes).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "account": account,
                "name": name,
                "user": user,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        account = d.pop("account")

        name = d.pop("name")

        user = d.pop("user")

        notes = d.pop("notes", UNSET)

        integration_request = cls(
            id=id,
            account=account,
            name=name,
            user=user,
            notes=notes,
        )

        integration_request.additional_properties = d
        return integration_request

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

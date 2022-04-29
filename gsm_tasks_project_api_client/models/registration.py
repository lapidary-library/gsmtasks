import json
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.registration_account import RegistrationAccount
from ..models.registration_user import RegistrationUser
from ..types import Unset

T = TypeVar("T", bound="Registration")


@attr.s(auto_attribs=True)
class Registration:
    """
    Attributes:
        account (RegistrationAccount):
        user (RegistrationUser):
        token (str):
    """

    account: RegistrationAccount
    user: RegistrationUser
    token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account = self.account.to_dict()

        user = self.user.to_dict()

        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "user": user,
                "token": token,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        account = (None, json.dumps(self.account.to_dict()).encode(), "application/json")

        user = (None, json.dumps(self.user.to_dict()).encode(), "application/json")

        token = self.token if isinstance(self.token, Unset) else (None, str(self.token).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "account": account,
                "user": user,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account = RegistrationAccount.from_dict(d.pop("account"))

        user = RegistrationUser.from_dict(d.pop("user"))

        token = d.pop("token")

        registration = cls(
            account=account,
            user=user,
            token=token,
        )

        registration.additional_properties = d
        return registration

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

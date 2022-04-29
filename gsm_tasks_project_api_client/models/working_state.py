import datetime
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.mode_enum import ModeEnum
from ..models.status_enum import StatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkingState")


@attr.s(auto_attribs=True)
class WorkingState:
    """
    Attributes:
        status (StatusEnum):
        created_at (datetime.datetime):
        account_role (Union[Unset, str]):
        account (Union[Unset, str]):
        user (Union[Unset, str]):
        mode (Union[Unset, ModeEnum]):
        timestamp (Union[Unset, datetime.datetime]):
    """

    status: StatusEnum
    created_at: datetime.datetime
    account_role: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    mode: Union[Unset, ModeEnum] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        created_at = self.created_at.isoformat()

        account_role = self.account_role
        account = self.account
        user = self.user
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "created_at": created_at,
            }
        )
        if account_role is not UNSET:
            field_dict["account_role"] = account_role
        if account is not UNSET:
            field_dict["account"] = account
        if user is not UNSET:
            field_dict["user"] = user
        if mode is not UNSET:
            field_dict["mode"] = mode
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        status = (None, str(self.status.value).encode(), "text/plain")

        created_at = self.created_at.isoformat().encode()

        account_role = (
            self.account_role
            if isinstance(self.account_role, Unset)
            else (None, str(self.account_role).encode(), "text/plain")
        )
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        mode: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.mode, Unset):
            mode = (None, str(self.mode.value).encode(), "text/plain")

        timestamp: Union[Unset, bytes] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat().encode()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "status": status,
                "created_at": created_at,
            }
        )
        if account_role is not UNSET:
            field_dict["account_role"] = account_role
        if account is not UNSET:
            field_dict["account"] = account
        if user is not UNSET:
            field_dict["user"] = user
        if mode is not UNSET:
            field_dict["mode"] = mode
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = StatusEnum(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        account_role = d.pop("account_role", UNSET)

        account = d.pop("account", UNSET)

        user = d.pop("user", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, ModeEnum]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = ModeEnum(_mode)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        working_state = cls(
            status=status,
            created_at=created_at,
            account_role=account_role,
            account=account,
            user=user,
            mode=mode,
            timestamp=timestamp,
        )

        working_state.additional_properties = d
        return working_state

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

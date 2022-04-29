import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRoute")


@attr.s(auto_attribs=True)
class PatchedRoute:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        external_id (Union[Unset, None, str]):
        account (Union[Unset, str]):
        code (Union[Unset, str]):
        description (Union[Unset, str]):
        assignee (Union[Unset, str]):
        start_time (Union[Unset, None, datetime.datetime]):
        start_location (Union[Unset, None, str]):
        end_time (Union[Unset, None, datetime.datetime]):
        end_location (Union[Unset, None, str]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    account: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    assignee: Union[Unset, str] = UNSET
    start_time: Union[Unset, None, datetime.datetime] = UNSET
    start_location: Union[Unset, None, str] = UNSET
    end_time: Union[Unset, None, datetime.datetime] = UNSET
    end_location: Union[Unset, None, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        external_id = self.external_id
        account = self.account
        code = self.code
        description = self.description
        assignee = self.assignee
        start_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat() if self.start_time else None

        start_location = self.start_location
        end_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat() if self.end_time else None

        end_location = self.end_location
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
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if start_location is not UNSET:
            field_dict["start_location"] = start_location
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if end_location is not UNSET:
            field_dict["end_location"] = end_location
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
        code = self.code if isinstance(self.code, Unset) else (None, str(self.code).encode(), "text/plain")
        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        assignee = (
            self.assignee if isinstance(self.assignee, Unset) else (None, str(self.assignee).encode(), "text/plain")
        )
        start_time: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat().encode() if self.start_time else None

        start_location = (
            self.start_location
            if isinstance(self.start_location, Unset)
            else (None, str(self.start_location).encode(), "text/plain")
        )
        end_time: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat().encode() if self.end_time else None

        end_location = (
            self.end_location
            if isinstance(self.end_location, Unset)
            else (None, str(self.end_location).encode(), "text/plain")
        )
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
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if start_location is not UNSET:
            field_dict["start_location"] = start_location
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if end_location is not UNSET:
            field_dict["end_location"] = end_location
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

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        assignee = d.pop("assignee", UNSET)

        _start_time = d.pop("start_time", UNSET)
        start_time: Union[Unset, None, datetime.datetime]
        if _start_time is None:
            start_time = None
        elif isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        start_location = d.pop("start_location", UNSET)

        _end_time = d.pop("end_time", UNSET)
        end_time: Union[Unset, None, datetime.datetime]
        if _end_time is None:
            end_time = None
        elif isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        end_location = d.pop("end_location", UNSET)

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

        patched_route = cls(
            id=id,
            url=url,
            external_id=external_id,
            account=account,
            code=code,
            description=description,
            assignee=assignee,
            start_time=start_time,
            start_location=start_location,
            end_time=end_time,
            end_location=end_location,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_route.additional_properties = d
        return patched_route

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

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Route")


@attr.s(auto_attribs=True)
class Route:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        code (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        external_id (Union[Unset, None, str]):
        description (Union[Unset, str]):
        assignee (Union[Unset, str]):
        start_time (Union[Unset, None, datetime.datetime]):
        start_location (Union[Unset, None, str]):
        end_time (Union[Unset, None, datetime.datetime]):
        end_location (Union[Unset, None, str]):
    """

    id: str
    url: str
    account: str
    code: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    external_id: Union[Unset, None, str] = UNSET
    description: Union[Unset, str] = UNSET
    assignee: Union[Unset, str] = UNSET
    start_time: Union[Unset, None, datetime.datetime] = UNSET
    start_location: Union[Unset, None, str] = UNSET
    end_time: Union[Unset, None, datetime.datetime] = UNSET
    end_location: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        code = self.code
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        external_id = self.external_id
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "code": code,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
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

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        code = self.code if isinstance(self.code, Unset) else (None, str(self.code).encode(), "text/plain")
        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        external_id = (
            self.external_id
            if isinstance(self.external_id, Unset)
            else (None, str(self.external_id).encode(), "text/plain")
        )
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "code": code,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        code = d.pop("code")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        external_id = d.pop("external_id", UNSET)

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

        route = cls(
            id=id,
            url=url,
            account=account,
            code=code,
            created_at=created_at,
            updated_at=updated_at,
            external_id=external_id,
            description=description,
            assignee=assignee,
            start_time=start_time,
            start_location=start_location,
            end_time=end_time,
            end_location=end_location,
        )

        route.additional_properties = d
        return route

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

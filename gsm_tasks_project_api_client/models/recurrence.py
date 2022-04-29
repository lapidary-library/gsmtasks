import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.recurrence_tasks_data import RecurrenceTasksData
from ..models.timezone_enum import TimezoneEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Recurrence")


@attr.s(auto_attribs=True)
class Recurrence:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        order (str):
        rrule (str):
        last_recurred_at (datetime.datetime):
        last_scheduled_at (datetime.datetime):
        next_scheduled_at (datetime.datetime):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        assign_worker (Union[Unset, bool]):
        is_active (Union[Unset, bool]):  Default: True.
        timezone (Union[Unset, TimezoneEnum]):
        tasks_data (Union[Unset, RecurrenceTasksData]):
    """

    id: str
    url: str
    account: str
    order: str
    rrule: str
    last_recurred_at: datetime.datetime
    last_scheduled_at: datetime.datetime
    next_scheduled_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    assign_worker: Union[Unset, bool] = False
    is_active: Union[Unset, bool] = True
    timezone: Union[Unset, TimezoneEnum] = UNSET
    tasks_data: Union[Unset, RecurrenceTasksData] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        order = self.order
        rrule = self.rrule
        last_recurred_at = self.last_recurred_at.isoformat()

        last_scheduled_at = self.last_scheduled_at.isoformat()

        next_scheduled_at = self.next_scheduled_at.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        assign_worker = self.assign_worker
        is_active = self.is_active
        timezone: Union[Unset, str] = UNSET
        if not isinstance(self.timezone, Unset):
            timezone = self.timezone.value

        tasks_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tasks_data, Unset):
            tasks_data = self.tasks_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "order": order,
                "rrule": rrule,
                "last_recurred_at": last_recurred_at,
                "last_scheduled_at": last_scheduled_at,
                "next_scheduled_at": next_scheduled_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if assign_worker is not UNSET:
            field_dict["assign_worker"] = assign_worker
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if tasks_data is not UNSET:
            field_dict["tasks_data"] = tasks_data

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        order = self.order if isinstance(self.order, Unset) else (None, str(self.order).encode(), "text/plain")
        rrule = self.rrule if isinstance(self.rrule, Unset) else (None, str(self.rrule).encode(), "text/plain")
        last_recurred_at = self.last_recurred_at.isoformat().encode()

        last_scheduled_at = self.last_scheduled_at.isoformat().encode()

        next_scheduled_at = self.next_scheduled_at.isoformat().encode()

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        assign_worker = (
            self.assign_worker
            if isinstance(self.assign_worker, Unset)
            else (None, str(self.assign_worker).encode(), "text/plain")
        )
        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )
        timezone: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.timezone, Unset):
            timezone = (None, str(self.timezone.value).encode(), "text/plain")

        tasks_data: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tasks_data, Unset):
            tasks_data = (None, json.dumps(self.tasks_data.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "order": order,
                "rrule": rrule,
                "last_recurred_at": last_recurred_at,
                "last_scheduled_at": last_scheduled_at,
                "next_scheduled_at": next_scheduled_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if assign_worker is not UNSET:
            field_dict["assign_worker"] = assign_worker
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if tasks_data is not UNSET:
            field_dict["tasks_data"] = tasks_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        order = d.pop("order")

        rrule = d.pop("rrule")

        last_recurred_at = isoparse(d.pop("last_recurred_at"))

        last_scheduled_at = isoparse(d.pop("last_scheduled_at"))

        next_scheduled_at = isoparse(d.pop("next_scheduled_at"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        assign_worker = d.pop("assign_worker", UNSET)

        is_active = d.pop("is_active", UNSET)

        _timezone = d.pop("timezone", UNSET)
        timezone: Union[Unset, TimezoneEnum]
        if isinstance(_timezone, Unset):
            timezone = UNSET
        else:
            timezone = TimezoneEnum(_timezone)

        _tasks_data = d.pop("tasks_data", UNSET)
        tasks_data: Union[Unset, RecurrenceTasksData]
        if isinstance(_tasks_data, Unset):
            tasks_data = UNSET
        else:
            tasks_data = RecurrenceTasksData.from_dict(_tasks_data)

        recurrence = cls(
            id=id,
            url=url,
            account=account,
            order=order,
            rrule=rrule,
            last_recurred_at=last_recurred_at,
            last_scheduled_at=last_scheduled_at,
            next_scheduled_at=next_scheduled_at,
            created_at=created_at,
            updated_at=updated_at,
            assign_worker=assign_worker,
            is_active=is_active,
            timezone=timezone,
            tasks_data=tasks_data,
        )

        recurrence.additional_properties = d
        return recurrence

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

import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.action_enum import ActionEnum
from ..models.task_command_location import TaskCommandLocation
from ..models.task_command_state_enum import TaskCommandStateEnum
from ..models.task_command_task_data import TaskCommandTaskData
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskCommand")


@attr.s(auto_attribs=True)
class TaskCommand:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        task (str):
        time (datetime.datetime):
        action (ActionEnum):
        user (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        external_id (Union[Unset, None, str]):
        notes (Union[Unset, str]): Task command notes
        location (Union[Unset, None, TaskCommandLocation]):
        assignee (Union[Unset, None, str]):
        state (Union[Unset, TaskCommandStateEnum]):
        error_message (Union[Unset, str]):
        task_data (Union[Unset, TaskCommandTaskData]):
        accepted_at (Union[Unset, None, datetime.datetime]):
        rejected_at (Union[Unset, None, datetime.datetime]):
    """

    id: str
    url: str
    account: str
    task: str
    time: datetime.datetime
    action: ActionEnum
    user: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    external_id: Union[Unset, None, str] = UNSET
    notes: Union[Unset, str] = UNSET
    location: Union[Unset, None, TaskCommandLocation] = UNSET
    assignee: Union[Unset, None, str] = UNSET
    state: Union[Unset, TaskCommandStateEnum] = UNSET
    error_message: Union[Unset, str] = UNSET
    task_data: Union[Unset, TaskCommandTaskData] = UNSET
    accepted_at: Union[Unset, None, datetime.datetime] = UNSET
    rejected_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        task = self.task
        time = self.time.isoformat()

        action = self.action.value

        user = self.user
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        external_id = self.external_id
        notes = self.notes
        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        assignee = self.assignee
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        error_message = self.error_message
        task_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.task_data, Unset):
            task_data = self.task_data.to_dict()

        accepted_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.accepted_at, Unset):
            accepted_at = self.accepted_at.isoformat() if self.accepted_at else None

        rejected_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.rejected_at, Unset):
            rejected_at = self.rejected_at.isoformat() if self.rejected_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "task": task,
                "time": time,
                "action": action,
                "user": user,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if location is not UNSET:
            field_dict["location"] = location
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if state is not UNSET:
            field_dict["state"] = state
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if task_data is not UNSET:
            field_dict["task_data"] = task_data
        if accepted_at is not UNSET:
            field_dict["accepted_at"] = accepted_at
        if rejected_at is not UNSET:
            field_dict["rejected_at"] = rejected_at

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        task = self.task if isinstance(self.task, Unset) else (None, str(self.task).encode(), "text/plain")
        time = self.time.isoformat().encode()

        action = (None, str(self.action.value).encode(), "text/plain")

        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        external_id = (
            self.external_id
            if isinstance(self.external_id, Unset)
            else (None, str(self.external_id).encode(), "text/plain")
        )
        notes = self.notes if isinstance(self.notes, Unset) else (None, str(self.notes).encode(), "text/plain")
        location: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.location, Unset):
            location = (
                (None, json.dumps(self.location.to_dict()).encode(), "application/json") if self.location else None
            )

        assignee = (
            self.assignee if isinstance(self.assignee, Unset) else (None, str(self.assignee).encode(), "text/plain")
        )
        state: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.state, Unset):
            state = (None, str(self.state.value).encode(), "text/plain")

        error_message = (
            self.error_message
            if isinstance(self.error_message, Unset)
            else (None, str(self.error_message).encode(), "text/plain")
        )
        task_data: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.task_data, Unset):
            task_data = (None, json.dumps(self.task_data.to_dict()).encode(), "application/json")

        accepted_at: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.accepted_at, Unset):
            accepted_at = self.accepted_at.isoformat().encode() if self.accepted_at else None

        rejected_at: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.rejected_at, Unset):
            rejected_at = self.rejected_at.isoformat().encode() if self.rejected_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "task": task,
                "time": time,
                "action": action,
                "user": user,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if location is not UNSET:
            field_dict["location"] = location
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if state is not UNSET:
            field_dict["state"] = state
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if task_data is not UNSET:
            field_dict["task_data"] = task_data
        if accepted_at is not UNSET:
            field_dict["accepted_at"] = accepted_at
        if rejected_at is not UNSET:
            field_dict["rejected_at"] = rejected_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        task = d.pop("task")

        time = isoparse(d.pop("time"))

        action = ActionEnum(d.pop("action"))

        user = d.pop("user")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        external_id = d.pop("external_id", UNSET)

        notes = d.pop("notes", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, None, TaskCommandLocation]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = TaskCommandLocation.from_dict(_location)

        assignee = d.pop("assignee", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, TaskCommandStateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = TaskCommandStateEnum(_state)

        error_message = d.pop("error_message", UNSET)

        _task_data = d.pop("task_data", UNSET)
        task_data: Union[Unset, TaskCommandTaskData]
        if isinstance(_task_data, Unset):
            task_data = UNSET
        else:
            task_data = TaskCommandTaskData.from_dict(_task_data)

        _accepted_at = d.pop("accepted_at", UNSET)
        accepted_at: Union[Unset, None, datetime.datetime]
        if _accepted_at is None:
            accepted_at = None
        elif isinstance(_accepted_at, Unset):
            accepted_at = UNSET
        else:
            accepted_at = isoparse(_accepted_at)

        _rejected_at = d.pop("rejected_at", UNSET)
        rejected_at: Union[Unset, None, datetime.datetime]
        if _rejected_at is None:
            rejected_at = None
        elif isinstance(_rejected_at, Unset):
            rejected_at = UNSET
        else:
            rejected_at = isoparse(_rejected_at)

        task_command = cls(
            id=id,
            url=url,
            account=account,
            task=task,
            time=time,
            action=action,
            user=user,
            created_at=created_at,
            updated_at=updated_at,
            external_id=external_id,
            notes=notes,
            location=location,
            assignee=assignee,
            state=state,
            error_message=error_message,
            task_data=task_data,
            accepted_at=accepted_at,
            rejected_at=rejected_at,
        )

        task_command.additional_properties = d
        return task_command

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

import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.state_e9a_enum import StateE9AEnum
from ..models.tasks_background_import_errors import TasksBackgroundImportErrors
from ..models.tasks_background_import_tasks_data_item import TasksBackgroundImportTasksDataItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="TasksBackgroundImport")


@attr.s(auto_attribs=True)
class TasksBackgroundImport:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        created_by (str):
        tasks_data (List[TasksBackgroundImportTasksDataItem]):
        state (StateE9AEnum):
        started_at (datetime.datetime):
        completed_at (datetime.datetime):
        failed_at (datetime.datetime):
        tasks_created (List[str]):
        assignees (List[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        errors (Union[Unset, TasksBackgroundImportErrors]):
        celery_task_id (Union[Unset, None, str]):
    """

    id: str
    url: str
    account: str
    created_by: str
    tasks_data: List[TasksBackgroundImportTasksDataItem]
    state: StateE9AEnum
    started_at: datetime.datetime
    completed_at: datetime.datetime
    failed_at: datetime.datetime
    tasks_created: List[str]
    assignees: List[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    errors: Union[Unset, TasksBackgroundImportErrors] = UNSET
    celery_task_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        created_by = self.created_by
        tasks_data = []
        for tasks_data_item_data in self.tasks_data:
            tasks_data_item = tasks_data_item_data.to_dict()

            tasks_data.append(tasks_data_item)

        state = self.state.value

        started_at = self.started_at.isoformat()

        completed_at = self.completed_at.isoformat()

        failed_at = self.failed_at.isoformat()

        tasks_created = self.tasks_created

        assignees = self.assignees

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        errors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        celery_task_id = self.celery_task_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "created_by": created_by,
                "tasks_data": tasks_data,
                "state": state,
                "started_at": started_at,
                "completed_at": completed_at,
                "failed_at": failed_at,
                "tasks_created": tasks_created,
                "assignees": assignees,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors
        if celery_task_id is not UNSET:
            field_dict["celery_task_id"] = celery_task_id

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        created_by = (
            self.created_by
            if isinstance(self.created_by, Unset)
            else (None, str(self.created_by).encode(), "text/plain")
        )
        _temp_tasks_data = []
        for tasks_data_item_data in self.tasks_data:
            tasks_data_item = tasks_data_item_data.to_dict()

            _temp_tasks_data.append(tasks_data_item)
        tasks_data = (None, json.dumps(_temp_tasks_data).encode(), "application/json")

        state = (None, str(self.state.value).encode(), "text/plain")

        started_at = self.started_at.isoformat().encode()

        completed_at = self.completed_at.isoformat().encode()

        failed_at = self.failed_at.isoformat().encode()

        _temp_tasks_created = self.tasks_created
        tasks_created = (None, json.dumps(_temp_tasks_created).encode(), "application/json")

        _temp_assignees = self.assignees
        assignees = (None, json.dumps(_temp_assignees).encode(), "application/json")

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        errors: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = (None, json.dumps(self.errors.to_dict()).encode(), "application/json")

        celery_task_id = (
            self.celery_task_id
            if isinstance(self.celery_task_id, Unset)
            else (None, str(self.celery_task_id).encode(), "text/plain")
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
                "created_by": created_by,
                "tasks_data": tasks_data,
                "state": state,
                "started_at": started_at,
                "completed_at": completed_at,
                "failed_at": failed_at,
                "tasks_created": tasks_created,
                "assignees": assignees,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors
        if celery_task_id is not UNSET:
            field_dict["celery_task_id"] = celery_task_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        created_by = d.pop("created_by")

        tasks_data = []
        _tasks_data = d.pop("tasks_data")
        for tasks_data_item_data in _tasks_data:
            tasks_data_item = TasksBackgroundImportTasksDataItem.from_dict(tasks_data_item_data)

            tasks_data.append(tasks_data_item)

        state = StateE9AEnum(d.pop("state"))

        started_at = isoparse(d.pop("started_at"))

        completed_at = isoparse(d.pop("completed_at"))

        failed_at = isoparse(d.pop("failed_at"))

        tasks_created = cast(List[str], d.pop("tasks_created"))

        assignees = cast(List[str], d.pop("assignees"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        _errors = d.pop("errors", UNSET)
        errors: Union[Unset, TasksBackgroundImportErrors]
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = TasksBackgroundImportErrors.from_dict(_errors)

        celery_task_id = d.pop("celery_task_id", UNSET)

        tasks_background_import = cls(
            id=id,
            url=url,
            account=account,
            created_by=created_by,
            tasks_data=tasks_data,
            state=state,
            started_at=started_at,
            completed_at=completed_at,
            failed_at=failed_at,
            tasks_created=tasks_created,
            assignees=assignees,
            created_at=created_at,
            updated_at=updated_at,
            errors=errors,
            celery_task_id=celery_task_id,
        )

        tasks_background_import.additional_properties = d
        return tasks_background_import

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

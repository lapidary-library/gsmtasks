import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.nested_contact import NestedContact
from ..models.task_serializer_v2 import TaskSerializerV2
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedOrderSerializerV2")


@attr.s(auto_attribs=True)
class PatchedOrderSerializerV2:
    """
    Attributes:
        id (Union[Unset, None, str]):
        url (Union[Unset, str]):
        account (Union[Unset, str]):
        external_id (Union[Unset, None, str]):
        reference (Union[Unset, str]):
        client (Union[Unset, str]):
        orderer (Union[Unset, NestedContact]):
        tasks (Union[Unset, List[str]]):
        tasks_data (Union[Unset, List[TaskSerializerV2]]):
        assignee (Union[Unset, str]):
        auto_assign (Union[Unset, bool]):
        created_by (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, None, str] = UNSET
    url: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    reference: Union[Unset, str] = UNSET
    client: Union[Unset, str] = UNSET
    orderer: Union[Unset, NestedContact] = UNSET
    tasks: Union[Unset, List[str]] = UNSET
    tasks_data: Union[Unset, List[TaskSerializerV2]] = UNSET
    assignee: Union[Unset, str] = UNSET
    auto_assign: Union[Unset, bool] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        external_id = self.external_id
        reference = self.reference
        client = self.client
        orderer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.orderer, Unset):
            orderer = self.orderer.to_dict()

        tasks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = self.tasks

        tasks_data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks_data, Unset):
            tasks_data = []
            for tasks_data_item_data in self.tasks_data:
                tasks_data_item = tasks_data_item_data.to_dict()

                tasks_data.append(tasks_data_item)

        assignee = self.assignee
        auto_assign = self.auto_assign
        created_by = self.created_by
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
        if account is not UNSET:
            field_dict["account"] = account
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if client is not UNSET:
            field_dict["client"] = client
        if orderer is not UNSET:
            field_dict["orderer"] = orderer
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if tasks_data is not UNSET:
            field_dict["tasks_data"] = tasks_data
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if auto_assign is not UNSET:
            field_dict["auto_assign"] = auto_assign
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        external_id = (
            self.external_id
            if isinstance(self.external_id, Unset)
            else (None, str(self.external_id).encode(), "text/plain")
        )
        reference = (
            self.reference if isinstance(self.reference, Unset) else (None, str(self.reference).encode(), "text/plain")
        )
        client = self.client if isinstance(self.client, Unset) else (None, str(self.client).encode(), "text/plain")
        orderer: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.orderer, Unset):
            orderer = (None, json.dumps(self.orderer.to_dict()).encode(), "application/json")

        tasks: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tasks, Unset):
            _temp_tasks = self.tasks
            tasks = (None, json.dumps(_temp_tasks).encode(), "application/json")

        tasks_data: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tasks_data, Unset):
            _temp_tasks_data = []
            for tasks_data_item_data in self.tasks_data:
                tasks_data_item = tasks_data_item_data.to_dict()

                _temp_tasks_data.append(tasks_data_item)
            tasks_data = (None, json.dumps(_temp_tasks_data).encode(), "application/json")

        assignee = (
            self.assignee if isinstance(self.assignee, Unset) else (None, str(self.assignee).encode(), "text/plain")
        )
        auto_assign = (
            self.auto_assign
            if isinstance(self.auto_assign, Unset)
            else (None, str(self.auto_assign).encode(), "text/plain")
        )
        created_by = (
            self.created_by
            if isinstance(self.created_by, Unset)
            else (None, str(self.created_by).encode(), "text/plain")
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
        if account is not UNSET:
            field_dict["account"] = account
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if client is not UNSET:
            field_dict["client"] = client
        if orderer is not UNSET:
            field_dict["orderer"] = orderer
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if tasks_data is not UNSET:
            field_dict["tasks_data"] = tasks_data
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if auto_assign is not UNSET:
            field_dict["auto_assign"] = auto_assign
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
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

        account = d.pop("account", UNSET)

        external_id = d.pop("external_id", UNSET)

        reference = d.pop("reference", UNSET)

        client = d.pop("client", UNSET)

        _orderer = d.pop("orderer", UNSET)
        orderer: Union[Unset, NestedContact]
        if isinstance(_orderer, Unset):
            orderer = UNSET
        else:
            orderer = NestedContact.from_dict(_orderer)

        tasks = cast(List[str], d.pop("tasks", UNSET))

        tasks_data = []
        _tasks_data = d.pop("tasks_data", UNSET)
        for tasks_data_item_data in _tasks_data or []:
            tasks_data_item = TaskSerializerV2.from_dict(tasks_data_item_data)

            tasks_data.append(tasks_data_item)

        assignee = d.pop("assignee", UNSET)

        auto_assign = d.pop("auto_assign", UNSET)

        created_by = d.pop("created_by", UNSET)

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

        patched_order_serializer_v2 = cls(
            id=id,
            url=url,
            account=account,
            external_id=external_id,
            reference=reference,
            client=client,
            orderer=orderer,
            tasks=tasks,
            tasks_data=tasks_data,
            assignee=assignee,
            auto_assign=auto_assign,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_order_serializer_v2.additional_properties = d
        return patched_order_serializer_v2

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

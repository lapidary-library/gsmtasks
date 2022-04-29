import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.account_user import AccountUser
from ..models.dashboard_scene_assigned_task_counts import DashboardSceneAssignedTaskCounts
from ..models.legacy_task import LegacyTask
from ..models.order import Order
from ..models.task_metadata import TaskMetadata
from ..models.worker_feature import WorkerFeature

T = TypeVar("T", bound="DashboardScene")


@attr.s(auto_attribs=True)
class DashboardScene:
    """
    Attributes:
        orders (List[Order]):
        tasks (List[LegacyTask]):
        task_metadatas (List[TaskMetadata]):
        assigned_task_counts (DashboardSceneAssignedTaskCounts):
        workers (List[AccountUser]):
        worker_features (List[WorkerFeature]):
        updated_at (datetime.datetime):
    """

    orders: List[Order]
    tasks: List[LegacyTask]
    task_metadatas: List[TaskMetadata]
    assigned_task_counts: DashboardSceneAssignedTaskCounts
    workers: List[AccountUser]
    worker_features: List[WorkerFeature]
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        orders = []
        for orders_item_data in self.orders:
            orders_item = orders_item_data.to_dict()

            orders.append(orders_item)

        tasks = []
        for tasks_item_data in self.tasks:
            tasks_item = tasks_item_data.to_dict()

            tasks.append(tasks_item)

        task_metadatas = []
        for task_metadatas_item_data in self.task_metadatas:
            task_metadatas_item = task_metadatas_item_data.to_dict()

            task_metadatas.append(task_metadatas_item)

        assigned_task_counts = self.assigned_task_counts.to_dict()

        workers = []
        for workers_item_data in self.workers:
            workers_item = workers_item_data.to_dict()

            workers.append(workers_item)

        worker_features = []
        for worker_features_item_data in self.worker_features:
            worker_features_item = worker_features_item_data.to_dict()

            worker_features.append(worker_features_item)

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orders": orders,
                "tasks": tasks,
                "task_metadatas": task_metadatas,
                "assigned_task_counts": assigned_task_counts,
                "workers": workers,
                "worker_features": worker_features,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        orders = []
        _orders = d.pop("orders")
        for orders_item_data in _orders:
            orders_item = Order.from_dict(orders_item_data)

            orders.append(orders_item)

        tasks = []
        _tasks = d.pop("tasks")
        for tasks_item_data in _tasks:
            tasks_item = LegacyTask.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        task_metadatas = []
        _task_metadatas = d.pop("task_metadatas")
        for task_metadatas_item_data in _task_metadatas:
            task_metadatas_item = TaskMetadata.from_dict(task_metadatas_item_data)

            task_metadatas.append(task_metadatas_item)

        assigned_task_counts = DashboardSceneAssignedTaskCounts.from_dict(d.pop("assigned_task_counts"))

        workers = []
        _workers = d.pop("workers")
        for workers_item_data in _workers:
            workers_item = AccountUser.from_dict(workers_item_data)

            workers.append(workers_item)

        worker_features = []
        _worker_features = d.pop("worker_features")
        for worker_features_item_data in _worker_features:
            worker_features_item = WorkerFeature.from_dict(worker_features_item_data)

            worker_features.append(worker_features_item)

        updated_at = isoparse(d.pop("updated_at"))

        dashboard_scene = cls(
            orders=orders,
            tasks=tasks,
            task_metadatas=task_metadatas,
            assigned_task_counts=assigned_task_counts,
            workers=workers,
            worker_features=worker_features,
            updated_at=updated_at,
        )

        dashboard_scene.additional_properties = d
        return dashboard_scene

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

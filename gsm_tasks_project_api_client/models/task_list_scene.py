import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.client import Client
from ..models.legacy_task import LegacyTask
from ..models.order import Order
from ..models.public_user import PublicUser
from ..models.task_event import TaskEvent
from ..models.task_metadata import TaskMetadata

T = TypeVar("T", bound="TaskListScene")


@attr.s(auto_attribs=True)
class TaskListScene:
    """
    Attributes:
        clients (List[Client]):
        orders (List[Order]):
        tasks (List[LegacyTask]):
        task_metadatas (List[TaskMetadata]):
        task_events_with_notes (List[TaskEvent]):
        users (List[PublicUser]):
        updated_at (datetime.datetime):
    """

    clients: List[Client]
    orders: List[Order]
    tasks: List[LegacyTask]
    task_metadatas: List[TaskMetadata]
    task_events_with_notes: List[TaskEvent]
    users: List[PublicUser]
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clients = []
        for clients_item_data in self.clients:
            clients_item = clients_item_data.to_dict()

            clients.append(clients_item)

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

        task_events_with_notes = []
        for task_events_with_notes_item_data in self.task_events_with_notes:
            task_events_with_notes_item = task_events_with_notes_item_data.to_dict()

            task_events_with_notes.append(task_events_with_notes_item)

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()

            users.append(users_item)

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clients": clients,
                "orders": orders,
                "tasks": tasks,
                "task_metadatas": task_metadatas,
                "task_events_with_notes": task_events_with_notes,
                "users": users,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        clients = []
        _clients = d.pop("clients")
        for clients_item_data in _clients:
            clients_item = Client.from_dict(clients_item_data)

            clients.append(clients_item)

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

        task_events_with_notes = []
        _task_events_with_notes = d.pop("task_events_with_notes")
        for task_events_with_notes_item_data in _task_events_with_notes:
            task_events_with_notes_item = TaskEvent.from_dict(task_events_with_notes_item_data)

            task_events_with_notes.append(task_events_with_notes_item)

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = PublicUser.from_dict(users_item_data)

            users.append(users_item)

        updated_at = isoparse(d.pop("updated_at"))

        task_list_scene = cls(
            clients=clients,
            orders=orders,
            tasks=tasks,
            task_metadatas=task_metadatas,
            task_events_with_notes=task_events_with_notes,
            users=users,
            updated_at=updated_at,
        )

        task_list_scene.additional_properties = d
        return task_list_scene

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

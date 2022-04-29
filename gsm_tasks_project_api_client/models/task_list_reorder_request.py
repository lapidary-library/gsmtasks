from typing import Any, Dict, List, Optional, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="TaskListReorderRequest")


@attr.s(auto_attribs=True)
class TaskListReorderRequest:
    """
    Attributes:
        account (str):
        assign_tasks (List[str]):
        reorder_tasks (List[str]):
        assignee (Optional[str]):
    """

    account: str
    assign_tasks: List[str]
    reorder_tasks: List[str]
    assignee: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account = self.account
        assign_tasks = self.assign_tasks

        reorder_tasks = self.reorder_tasks

        assignee = self.assignee

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "assign_tasks": assign_tasks,
                "reorder_tasks": reorder_tasks,
                "assignee": assignee,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account = d.pop("account")

        assign_tasks = cast(List[str], d.pop("assign_tasks"))

        reorder_tasks = cast(List[str], d.pop("reorder_tasks"))

        assignee = d.pop("assignee")

        task_list_reorder_request = cls(
            account=account,
            assign_tasks=assign_tasks,
            reorder_tasks=reorder_tasks,
            assignee=assignee,
        )

        task_list_reorder_request.additional_properties = d
        return task_list_reorder_request

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

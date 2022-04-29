import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskForm")


@attr.s(auto_attribs=True)
class TaskForm:
    """
    Attributes:
        id (str):
        url (str):
        task (str):
        name (str):
        link (str):
        edit_url (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        view_url (Union[Unset, str]):
        pdf_url (Union[Unset, str]):
        completed (Union[Unset, bool]):
    """

    id: str
    url: str
    task: str
    name: str
    link: str
    edit_url: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    view_url: Union[Unset, str] = UNSET
    pdf_url: Union[Unset, str] = UNSET
    completed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        task = self.task
        name = self.name
        link = self.link
        edit_url = self.edit_url
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        view_url = self.view_url
        pdf_url = self.pdf_url
        completed = self.completed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "task": task,
                "name": name,
                "link": link,
                "edit_url": edit_url,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if view_url is not UNSET:
            field_dict["view_url"] = view_url
        if pdf_url is not UNSET:
            field_dict["pdf_url"] = pdf_url
        if completed is not UNSET:
            field_dict["completed"] = completed

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        task = self.task if isinstance(self.task, Unset) else (None, str(self.task).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        link = self.link if isinstance(self.link, Unset) else (None, str(self.link).encode(), "text/plain")
        edit_url = (
            self.edit_url if isinstance(self.edit_url, Unset) else (None, str(self.edit_url).encode(), "text/plain")
        )
        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        view_url = (
            self.view_url if isinstance(self.view_url, Unset) else (None, str(self.view_url).encode(), "text/plain")
        )
        pdf_url = self.pdf_url if isinstance(self.pdf_url, Unset) else (None, str(self.pdf_url).encode(), "text/plain")
        completed = (
            self.completed if isinstance(self.completed, Unset) else (None, str(self.completed).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "task": task,
                "name": name,
                "link": link,
                "edit_url": edit_url,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if view_url is not UNSET:
            field_dict["view_url"] = view_url
        if pdf_url is not UNSET:
            field_dict["pdf_url"] = pdf_url
        if completed is not UNSET:
            field_dict["completed"] = completed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        task = d.pop("task")

        name = d.pop("name")

        link = d.pop("link")

        edit_url = d.pop("edit_url")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        view_url = d.pop("view_url", UNSET)

        pdf_url = d.pop("pdf_url", UNSET)

        completed = d.pop("completed", UNSET)

        task_form = cls(
            id=id,
            url=url,
            task=task,
            name=name,
            link=link,
            edit_url=edit_url,
            created_at=created_at,
            updated_at=updated_at,
            view_url=view_url,
            pdf_url=pdf_url,
            completed=completed,
        )

        task_form.additional_properties = d
        return task_form

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

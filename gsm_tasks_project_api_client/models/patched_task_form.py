import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedTaskForm")


@attr.s(auto_attribs=True)
class PatchedTaskForm:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        task (Union[Unset, str]):
        name (Union[Unset, str]):
        link (Union[Unset, str]):
        edit_url (Union[Unset, str]):
        view_url (Union[Unset, str]):
        pdf_url (Union[Unset, str]):
        completed (Union[Unset, bool]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    task: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    edit_url: Union[Unset, str] = UNSET
    view_url: Union[Unset, str] = UNSET
    pdf_url: Union[Unset, str] = UNSET
    completed: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        task = self.task
        name = self.name
        link = self.link
        edit_url = self.edit_url
        view_url = self.view_url
        pdf_url = self.pdf_url
        completed = self.completed
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
        if task is not UNSET:
            field_dict["task"] = task
        if name is not UNSET:
            field_dict["name"] = name
        if link is not UNSET:
            field_dict["link"] = link
        if edit_url is not UNSET:
            field_dict["edit_url"] = edit_url
        if view_url is not UNSET:
            field_dict["view_url"] = view_url
        if pdf_url is not UNSET:
            field_dict["pdf_url"] = pdf_url
        if completed is not UNSET:
            field_dict["completed"] = completed
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

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
        view_url = (
            self.view_url if isinstance(self.view_url, Unset) else (None, str(self.view_url).encode(), "text/plain")
        )
        pdf_url = self.pdf_url if isinstance(self.pdf_url, Unset) else (None, str(self.pdf_url).encode(), "text/plain")
        completed = (
            self.completed if isinstance(self.completed, Unset) else (None, str(self.completed).encode(), "text/plain")
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
        if task is not UNSET:
            field_dict["task"] = task
        if name is not UNSET:
            field_dict["name"] = name
        if link is not UNSET:
            field_dict["link"] = link
        if edit_url is not UNSET:
            field_dict["edit_url"] = edit_url
        if view_url is not UNSET:
            field_dict["view_url"] = view_url
        if pdf_url is not UNSET:
            field_dict["pdf_url"] = pdf_url
        if completed is not UNSET:
            field_dict["completed"] = completed
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

        task = d.pop("task", UNSET)

        name = d.pop("name", UNSET)

        link = d.pop("link", UNSET)

        edit_url = d.pop("edit_url", UNSET)

        view_url = d.pop("view_url", UNSET)

        pdf_url = d.pop("pdf_url", UNSET)

        completed = d.pop("completed", UNSET)

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

        patched_task_form = cls(
            id=id,
            url=url,
            task=task,
            name=name,
            link=link,
            edit_url=edit_url,
            view_url=view_url,
            pdf_url=pdf_url,
            completed=completed,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_task_form.additional_properties = d
        return patched_task_form

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

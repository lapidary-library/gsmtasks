import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.source_enum import SourceEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Document")


@attr.s(auto_attribs=True)
class Document:
    """
    Attributes:
        id (str):
        url (str):
        file (str):
        file_name (str):
        created_by (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        account (Union[Unset, str]):
        external_id (Union[Unset, None, str]):
        order (Union[Unset, None, str]):
        task (Union[Unset, None, str]):
        file_upload (Union[Unset, None, str]):
        description (Union[Unset, str]):
        source (Union[BlankEnum, None, SourceEnum, Unset]):
        visible_to_worker (Union[Unset, bool]):
        visible_to_client (Union[Unset, bool]):
    """

    id: str
    url: str
    file: str
    file_name: str
    created_by: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    account: Union[Unset, str] = UNSET
    external_id: Union[Unset, None, str] = UNSET
    order: Union[Unset, None, str] = UNSET
    task: Union[Unset, None, str] = UNSET
    file_upload: Union[Unset, None, str] = UNSET
    description: Union[Unset, str] = UNSET
    source: Union[BlankEnum, None, SourceEnum, Unset] = UNSET
    visible_to_worker: Union[Unset, bool] = UNSET
    visible_to_client: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        file = self.file
        file_name = self.file_name
        created_by = self.created_by
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        account = self.account
        external_id = self.external_id
        order = self.order
        task = self.task
        file_upload = self.file_upload
        description = self.description
        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        elif self.source is None:
            source = None

        elif isinstance(self.source, SourceEnum):
            source = UNSET
            if not isinstance(self.source, Unset):
                source = self.source.value

        elif isinstance(self.source, BlankEnum):
            source = UNSET
            if not isinstance(self.source, Unset):
                source = self.source.value

        else:
            source = self.source

        visible_to_worker = self.visible_to_worker
        visible_to_client = self.visible_to_client

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "file": file,
                "file_name": file_name,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if account is not UNSET:
            field_dict["account"] = account
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if order is not UNSET:
            field_dict["order"] = order
        if task is not UNSET:
            field_dict["task"] = task
        if file_upload is not UNSET:
            field_dict["file_upload"] = file_upload
        if description is not UNSET:
            field_dict["description"] = description
        if source is not UNSET:
            field_dict["source"] = source
        if visible_to_worker is not UNSET:
            field_dict["visible_to_worker"] = visible_to_worker
        if visible_to_client is not UNSET:
            field_dict["visible_to_client"] = visible_to_client

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        file = self.file if isinstance(self.file, Unset) else (None, str(self.file).encode(), "text/plain")
        file_name = (
            self.file_name if isinstance(self.file_name, Unset) else (None, str(self.file_name).encode(), "text/plain")
        )
        created_by = (
            self.created_by
            if isinstance(self.created_by, Unset)
            else (None, str(self.created_by).encode(), "text/plain")
        )
        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        external_id = (
            self.external_id
            if isinstance(self.external_id, Unset)
            else (None, str(self.external_id).encode(), "text/plain")
        )
        order = self.order if isinstance(self.order, Unset) else (None, str(self.order).encode(), "text/plain")
        task = self.task if isinstance(self.task, Unset) else (None, str(self.task).encode(), "text/plain")
        file_upload = (
            self.file_upload
            if isinstance(self.file_upload, Unset)
            else (None, str(self.file_upload).encode(), "text/plain")
        )
        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        elif self.source is None:
            source = None

        elif isinstance(self.source, SourceEnum):
            source = UNSET
            if not isinstance(self.source, Unset):
                source = (None, str(self.source.value).encode(), "text/plain")

        elif isinstance(self.source, BlankEnum):
            source = UNSET
            if not isinstance(self.source, Unset):
                source = (None, str(self.source.value).encode(), "text/plain")

        else:
            source = self.source

        visible_to_worker = (
            self.visible_to_worker
            if isinstance(self.visible_to_worker, Unset)
            else (None, str(self.visible_to_worker).encode(), "text/plain")
        )
        visible_to_client = (
            self.visible_to_client
            if isinstance(self.visible_to_client, Unset)
            else (None, str(self.visible_to_client).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "file": file,
                "file_name": file_name,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if account is not UNSET:
            field_dict["account"] = account
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if order is not UNSET:
            field_dict["order"] = order
        if task is not UNSET:
            field_dict["task"] = task
        if file_upload is not UNSET:
            field_dict["file_upload"] = file_upload
        if description is not UNSET:
            field_dict["description"] = description
        if source is not UNSET:
            field_dict["source"] = source
        if visible_to_worker is not UNSET:
            field_dict["visible_to_worker"] = visible_to_worker
        if visible_to_client is not UNSET:
            field_dict["visible_to_client"] = visible_to_client

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        file = d.pop("file")

        file_name = d.pop("file_name")

        created_by = d.pop("created_by")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        account = d.pop("account", UNSET)

        external_id = d.pop("external_id", UNSET)

        order = d.pop("order", UNSET)

        task = d.pop("task", UNSET)

        file_upload = d.pop("file_upload", UNSET)

        description = d.pop("description", UNSET)

        def _parse_source(data: object) -> Union[BlankEnum, None, SourceEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _source_type_0 = data
                source_type_0: Union[Unset, SourceEnum]
                if isinstance(_source_type_0, Unset):
                    source_type_0 = UNSET
                else:
                    source_type_0 = SourceEnum(_source_type_0)

                return source_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _source_type_1 = data
                source_type_1: Union[Unset, BlankEnum]
                if isinstance(_source_type_1, Unset):
                    source_type_1 = UNSET
                else:
                    source_type_1 = BlankEnum(_source_type_1)

                return source_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, None, SourceEnum, Unset], data)

        source = _parse_source(d.pop("source", UNSET))

        visible_to_worker = d.pop("visible_to_worker", UNSET)

        visible_to_client = d.pop("visible_to_client", UNSET)

        document = cls(
            id=id,
            url=url,
            file=file,
            file_name=file_name,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            account=account,
            external_id=external_id,
            order=order,
            task=task,
            file_upload=file_upload,
            description=description,
            source=source,
            visible_to_worker=visible_to_worker,
            visible_to_client=visible_to_client,
        )

        document.additional_properties = d
        return document

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

import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.nested_contact import NestedContact
from ..models.signature_location import SignatureLocation
from ..models.source_enum import SourceEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Signature")


@attr.s(auto_attribs=True)
class Signature:
    """
    Attributes:
        id (str):
        url (str):
        task (str):
        file_upload (str):
        file (str):
        file_name (str):
        signer (NestedContact):
        created_by (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        account (Union[Unset, str]):
        documents (Union[Unset, List[str]]):
        location (Union[Unset, None, SignatureLocation]):
        source (Union[BlankEnum, None, SourceEnum, Unset]):
    """

    id: str
    url: str
    task: str
    file_upload: str
    file: str
    file_name: str
    signer: NestedContact
    created_by: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    account: Union[Unset, str] = UNSET
    documents: Union[Unset, List[str]] = UNSET
    location: Union[Unset, None, SignatureLocation] = UNSET
    source: Union[BlankEnum, None, SourceEnum, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        task = self.task
        file_upload = self.file_upload
        file = self.file
        file_name = self.file_name
        signer = self.signer.to_dict()

        created_by = self.created_by
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        account = self.account
        documents: Union[Unset, List[str]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = self.documents

        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "task": task,
                "file_upload": file_upload,
                "file": file,
                "file_name": file_name,
                "signer": signer,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if account is not UNSET:
            field_dict["account"] = account
        if documents is not UNSET:
            field_dict["documents"] = documents
        if location is not UNSET:
            field_dict["location"] = location
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        task = self.task if isinstance(self.task, Unset) else (None, str(self.task).encode(), "text/plain")
        file_upload = (
            self.file_upload
            if isinstance(self.file_upload, Unset)
            else (None, str(self.file_upload).encode(), "text/plain")
        )
        file = self.file if isinstance(self.file, Unset) else (None, str(self.file).encode(), "text/plain")
        file_name = (
            self.file_name if isinstance(self.file_name, Unset) else (None, str(self.file_name).encode(), "text/plain")
        )
        signer = (None, json.dumps(self.signer.to_dict()).encode(), "application/json")

        created_by = (
            self.created_by
            if isinstance(self.created_by, Unset)
            else (None, str(self.created_by).encode(), "text/plain")
        )
        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        documents: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.documents, Unset):
            _temp_documents = self.documents
            documents = (None, json.dumps(_temp_documents).encode(), "application/json")

        location: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.location, Unset):
            location = (
                (None, json.dumps(self.location.to_dict()).encode(), "application/json") if self.location else None
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "task": task,
                "file_upload": file_upload,
                "file": file,
                "file_name": file_name,
                "signer": signer,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if account is not UNSET:
            field_dict["account"] = account
        if documents is not UNSET:
            field_dict["documents"] = documents
        if location is not UNSET:
            field_dict["location"] = location
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        task = d.pop("task")

        file_upload = d.pop("file_upload")

        file = d.pop("file")

        file_name = d.pop("file_name")

        signer = NestedContact.from_dict(d.pop("signer"))

        created_by = d.pop("created_by")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        account = d.pop("account", UNSET)

        documents = cast(List[str], d.pop("documents", UNSET))

        _location = d.pop("location", UNSET)
        location: Union[Unset, None, SignatureLocation]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = SignatureLocation.from_dict(_location)

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

        signature = cls(
            id=id,
            url=url,
            task=task,
            file_upload=file_upload,
            file=file,
            file_name=file_name,
            signer=signer,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            account=account,
            documents=documents,
            location=location,
            source=source,
        )

        signature.additional_properties = d
        return signature

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

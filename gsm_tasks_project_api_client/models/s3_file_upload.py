import datetime
import json
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.s3_file_upload_s3_signature import S3FileUploadS3Signature
from ..models.source_enum import SourceEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="S3FileUpload")


@attr.s(auto_attribs=True)
class S3FileUpload:
    """Saves either a file or file_url.
    in case S3 is used, it requires file name and file type and after save returns an upload url and saves the url.

    This serializer can not be used in other serializers if Amazon S3 upload is used.

        Attributes:
            id (str):
            url (str):
            file (str):
            file_name (str):
            file_type (str):
            created_by (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            s3_signature (Optional[S3FileUploadS3Signature]):
            source (Union[BlankEnum, None, SourceEnum, Unset]):
    """

    id: str
    url: str
    file: str
    file_name: str
    file_type: str
    created_by: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    s3_signature: Optional[S3FileUploadS3Signature]
    source: Union[BlankEnum, None, SourceEnum, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        file = self.file
        file_name = self.file_name
        file_type = self.file_type
        created_by = self.created_by
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        s3_signature = self.s3_signature.to_dict() if self.s3_signature else None

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
                "file": file,
                "file_name": file_name,
                "file_type": file_type,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
                "s3_signature": s3_signature,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        file = self.file if isinstance(self.file, Unset) else (None, str(self.file).encode(), "text/plain")
        file_name = (
            self.file_name if isinstance(self.file_name, Unset) else (None, str(self.file_name).encode(), "text/plain")
        )
        file_type = (
            self.file_type if isinstance(self.file_type, Unset) else (None, str(self.file_type).encode(), "text/plain")
        )
        created_by = (
            self.created_by
            if isinstance(self.created_by, Unset)
            else (None, str(self.created_by).encode(), "text/plain")
        )
        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        s3_signature = (
            (None, json.dumps(self.s3_signature.to_dict()).encode(), "application/json") if self.s3_signature else None
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
                "file": file,
                "file_name": file_name,
                "file_type": file_type,
                "created_by": created_by,
                "created_at": created_at,
                "updated_at": updated_at,
                "s3_signature": s3_signature,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        file = d.pop("file")

        file_name = d.pop("file_name")

        file_type = d.pop("file_type")

        created_by = d.pop("created_by")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        _s3_signature = d.pop("s3_signature")
        s3_signature: Optional[S3FileUploadS3Signature]
        if _s3_signature is None:
            s3_signature = None
        else:
            s3_signature = S3FileUploadS3Signature.from_dict(_s3_signature)

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

        s3_file_upload = cls(
            id=id,
            url=url,
            file=file,
            file_name=file_name,
            file_type=file_type,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            s3_signature=s3_signature,
            source=source,
        )

        s3_file_upload.additional_properties = d
        return s3_file_upload

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

import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.export_model_enum import ExportModelEnum
from ..models.format_enum import FormatEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedExport")


@attr.s(auto_attribs=True)
class PatchedExport:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        account (Union[Unset, str]):
        export_model (Union[Unset, ExportModelEnum]):
        field_names (Union[Unset, None, List[str]]):
        format_ (Union[Unset, FormatEnum]):
        link (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    export_model: Union[Unset, ExportModelEnum] = UNSET
    field_names: Union[Unset, None, List[str]] = UNSET
    format_: Union[Unset, FormatEnum] = UNSET
    link: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        export_model: Union[Unset, str] = UNSET
        if not isinstance(self.export_model, Unset):
            export_model = self.export_model.value

        field_names: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.field_names, Unset):
            if self.field_names is None:
                field_names = None
            else:
                field_names = self.field_names

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        link = self.link
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
        if export_model is not UNSET:
            field_dict["export_model"] = export_model
        if field_names is not UNSET:
            field_dict["field_names"] = field_names
        if format_ is not UNSET:
            field_dict["format"] = format_
        if link is not UNSET:
            field_dict["link"] = link
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        export_model: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.export_model, Unset):
            export_model = (None, str(self.export_model.value).encode(), "text/plain")

        field_names: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.field_names, Unset):
            if self.field_names is None:
                field_names = None
            else:
                _temp_field_names = self.field_names
                field_names = (None, json.dumps(_temp_field_names).encode(), "application/json")

        format_: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = (None, str(self.format_.value).encode(), "text/plain")

        link = self.link if isinstance(self.link, Unset) else (None, str(self.link).encode(), "text/plain")
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
        if export_model is not UNSET:
            field_dict["export_model"] = export_model
        if field_names is not UNSET:
            field_dict["field_names"] = field_names
        if format_ is not UNSET:
            field_dict["format"] = format_
        if link is not UNSET:
            field_dict["link"] = link
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

        _export_model = d.pop("export_model", UNSET)
        export_model: Union[Unset, ExportModelEnum]
        if isinstance(_export_model, Unset):
            export_model = UNSET
        else:
            export_model = ExportModelEnum(_export_model)

        field_names = cast(List[str], d.pop("field_names", UNSET))

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, FormatEnum]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = FormatEnum(_format_)

        link = d.pop("link", UNSET)

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

        patched_export = cls(
            id=id,
            url=url,
            account=account,
            export_model=export_model,
            field_names=field_names,
            format_=format_,
            link=link,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_export.additional_properties = d
        return patched_export

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

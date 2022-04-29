import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.export_model_enum import ExportModelEnum
from ..models.format_enum import FormatEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Export")


@attr.s(auto_attribs=True)
class Export:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        export_model (ExportModelEnum):
        format_ (FormatEnum):
        link (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        field_names (Union[Unset, None, List[str]]):
    """

    id: str
    url: str
    account: str
    export_model: ExportModelEnum
    format_: FormatEnum
    link: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    field_names: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        export_model = self.export_model.value

        format_ = self.format_.value

        link = self.link
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_names: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.field_names, Unset):
            if self.field_names is None:
                field_names = None
            else:
                field_names = self.field_names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "export_model": export_model,
                "format": format_,
                "link": link,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if field_names is not UNSET:
            field_dict["field_names"] = field_names

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        export_model = (None, str(self.export_model.value).encode(), "text/plain")

        format_ = (None, str(self.format_.value).encode(), "text/plain")

        link = self.link if isinstance(self.link, Unset) else (None, str(self.link).encode(), "text/plain")
        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        field_names: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.field_names, Unset):
            if self.field_names is None:
                field_names = None
            else:
                _temp_field_names = self.field_names
                field_names = (None, json.dumps(_temp_field_names).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "export_model": export_model,
                "format": format_,
                "link": link,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if field_names is not UNSET:
            field_dict["field_names"] = field_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        export_model = ExportModelEnum(d.pop("export_model"))

        format_ = FormatEnum(d.pop("format"))

        link = d.pop("link")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        field_names = cast(List[str], d.pop("field_names", UNSET))

        export = cls(
            id=id,
            url=url,
            account=account,
            export_model=export_model,
            format_=format_,
            link=link,
            created_at=created_at,
            updated_at=updated_at,
            field_names=field_names,
        )

        export.additional_properties = d
        return export

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

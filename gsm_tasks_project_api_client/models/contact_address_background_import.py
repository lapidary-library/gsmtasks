import datetime
import json
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

from ..models.contact_address_background_import_contact_addresses_data_item import (
    ContactAddressBackgroundImportContactAddressesDataItem,
)
from ..models.contact_address_background_import_errors import ContactAddressBackgroundImportErrors
from ..models.state_e9a_enum import StateE9AEnum
from ..types import Unset

T = TypeVar("T", bound="ContactAddressBackgroundImport")


@attr.s(auto_attribs=True)
class ContactAddressBackgroundImport:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        created_by (str):
        contact_addresses_data (List[ContactAddressBackgroundImportContactAddressesDataItem]):
        state (StateE9AEnum):
        started_at (datetime.datetime):
        completed_at (datetime.datetime):
        failed_at (datetime.datetime):
        errors (ContactAddressBackgroundImportErrors):
        celery_task_id (str):
        contact_addresses_created (List[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: str
    url: str
    account: str
    created_by: str
    contact_addresses_data: List[ContactAddressBackgroundImportContactAddressesDataItem]
    state: StateE9AEnum
    started_at: datetime.datetime
    completed_at: datetime.datetime
    failed_at: datetime.datetime
    errors: ContactAddressBackgroundImportErrors
    celery_task_id: str
    contact_addresses_created: List[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        created_by = self.created_by
        contact_addresses_data = []
        for contact_addresses_data_item_data in self.contact_addresses_data:
            contact_addresses_data_item = contact_addresses_data_item_data.to_dict()

            contact_addresses_data.append(contact_addresses_data_item)

        state = self.state.value

        started_at = self.started_at.isoformat()

        completed_at = self.completed_at.isoformat()

        failed_at = self.failed_at.isoformat()

        errors = self.errors.to_dict()

        celery_task_id = self.celery_task_id
        contact_addresses_created = self.contact_addresses_created

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "created_by": created_by,
                "contact_addresses_data": contact_addresses_data,
                "state": state,
                "started_at": started_at,
                "completed_at": completed_at,
                "failed_at": failed_at,
                "errors": errors,
                "celery_task_id": celery_task_id,
                "contact_addresses_created": contact_addresses_created,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        created_by = (
            self.created_by
            if isinstance(self.created_by, Unset)
            else (None, str(self.created_by).encode(), "text/plain")
        )
        _temp_contact_addresses_data = []
        for contact_addresses_data_item_data in self.contact_addresses_data:
            contact_addresses_data_item = contact_addresses_data_item_data.to_dict()

            _temp_contact_addresses_data.append(contact_addresses_data_item)
        contact_addresses_data = (None, json.dumps(_temp_contact_addresses_data).encode(), "application/json")

        state = (None, str(self.state.value).encode(), "text/plain")

        started_at = self.started_at.isoformat().encode()

        completed_at = self.completed_at.isoformat().encode()

        failed_at = self.failed_at.isoformat().encode()

        errors = (None, json.dumps(self.errors.to_dict()).encode(), "application/json")

        celery_task_id = (
            self.celery_task_id
            if isinstance(self.celery_task_id, Unset)
            else (None, str(self.celery_task_id).encode(), "text/plain")
        )
        _temp_contact_addresses_created = self.contact_addresses_created
        contact_addresses_created = (None, json.dumps(_temp_contact_addresses_created).encode(), "application/json")

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "created_by": created_by,
                "contact_addresses_data": contact_addresses_data,
                "state": state,
                "started_at": started_at,
                "completed_at": completed_at,
                "failed_at": failed_at,
                "errors": errors,
                "celery_task_id": celery_task_id,
                "contact_addresses_created": contact_addresses_created,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        created_by = d.pop("created_by")

        contact_addresses_data = []
        _contact_addresses_data = d.pop("contact_addresses_data")
        for contact_addresses_data_item_data in _contact_addresses_data:
            contact_addresses_data_item = ContactAddressBackgroundImportContactAddressesDataItem.from_dict(
                contact_addresses_data_item_data
            )

            contact_addresses_data.append(contact_addresses_data_item)

        state = StateE9AEnum(d.pop("state"))

        started_at = isoparse(d.pop("started_at"))

        completed_at = isoparse(d.pop("completed_at"))

        failed_at = isoparse(d.pop("failed_at"))

        errors = ContactAddressBackgroundImportErrors.from_dict(d.pop("errors"))

        celery_task_id = d.pop("celery_task_id")

        contact_addresses_created = cast(List[str], d.pop("contact_addresses_created"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        contact_address_background_import = cls(
            id=id,
            url=url,
            account=account,
            created_by=created_by,
            contact_addresses_data=contact_addresses_data,
            state=state,
            started_at=started_at,
            completed_at=completed_at,
            failed_at=failed_at,
            errors=errors,
            celery_task_id=celery_task_id,
            contact_addresses_created=contact_addresses_created,
            created_at=created_at,
            updated_at=updated_at,
        )

        contact_address_background_import.additional_properties = d
        return contact_address_background_import

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

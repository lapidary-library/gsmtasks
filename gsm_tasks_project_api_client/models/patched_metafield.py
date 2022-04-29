import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.value_type_enum import ValueTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedMetafield")


@attr.s(auto_attribs=True)
class PatchedMetafield:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        account (Union[Unset, str]):
        ordering (Union[Unset, int]):
        namespace (Union[Unset, str]):  Default: 'gsmtasks'.
        key (Union[Unset, str]):
        field_name (Union[Unset, str]):
        value_type (Union[Unset, ValueTypeEnum]):
        label (Union[Unset, str]):
        choices (Union[Unset, None, List[str]]):
        choices_url (Union[Unset, None, str]):
        is_editable (Union[Unset, bool]):
        is_editable_assignee (Union[Unset, bool]):
        is_required (Union[Unset, bool]):
        is_persistent (Union[Unset, bool]): Metadata, that will be copied to on recurrence.
        is_searchable (Union[Unset, bool]):
        show_in_list_view (Union[Unset, bool]):
        show_in_detail_view (Union[Unset, bool]):
        show_in_mobile_app (Union[Unset, bool]):
        show_in_pod (Union[Unset, bool]):
        show_when_task_type_assignment (Union[Unset, bool]):
        show_when_task_type_pick_up (Union[Unset, bool]):
        show_when_task_type_drop_off (Union[Unset, bool]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    ordering: Union[Unset, int] = UNSET
    namespace: Union[Unset, str] = "gsmtasks"
    key: Union[Unset, str] = UNSET
    field_name: Union[Unset, str] = UNSET
    value_type: Union[Unset, ValueTypeEnum] = UNSET
    label: Union[Unset, str] = UNSET
    choices: Union[Unset, None, List[str]] = UNSET
    choices_url: Union[Unset, None, str] = UNSET
    is_editable: Union[Unset, bool] = UNSET
    is_editable_assignee: Union[Unset, bool] = UNSET
    is_required: Union[Unset, bool] = UNSET
    is_persistent: Union[Unset, bool] = UNSET
    is_searchable: Union[Unset, bool] = UNSET
    show_in_list_view: Union[Unset, bool] = UNSET
    show_in_detail_view: Union[Unset, bool] = UNSET
    show_in_mobile_app: Union[Unset, bool] = UNSET
    show_in_pod: Union[Unset, bool] = UNSET
    show_when_task_type_assignment: Union[Unset, bool] = UNSET
    show_when_task_type_pick_up: Union[Unset, bool] = UNSET
    show_when_task_type_drop_off: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        ordering = self.ordering
        namespace = self.namespace
        key = self.key
        field_name = self.field_name
        value_type: Union[Unset, str] = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = self.value_type.value

        label = self.label
        choices: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.choices, Unset):
            if self.choices is None:
                choices = None
            else:
                choices = self.choices

        choices_url = self.choices_url
        is_editable = self.is_editable
        is_editable_assignee = self.is_editable_assignee
        is_required = self.is_required
        is_persistent = self.is_persistent
        is_searchable = self.is_searchable
        show_in_list_view = self.show_in_list_view
        show_in_detail_view = self.show_in_detail_view
        show_in_mobile_app = self.show_in_mobile_app
        show_in_pod = self.show_in_pod
        show_when_task_type_assignment = self.show_when_task_type_assignment
        show_when_task_type_pick_up = self.show_when_task_type_pick_up
        show_when_task_type_drop_off = self.show_when_task_type_drop_off
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
        if ordering is not UNSET:
            field_dict["ordering"] = ordering
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if key is not UNSET:
            field_dict["key"] = key
        if field_name is not UNSET:
            field_dict["field_name"] = field_name
        if value_type is not UNSET:
            field_dict["value_type"] = value_type
        if label is not UNSET:
            field_dict["label"] = label
        if choices is not UNSET:
            field_dict["choices"] = choices
        if choices_url is not UNSET:
            field_dict["choices_url"] = choices_url
        if is_editable is not UNSET:
            field_dict["is_editable"] = is_editable
        if is_editable_assignee is not UNSET:
            field_dict["is_editable_assignee"] = is_editable_assignee
        if is_required is not UNSET:
            field_dict["is_required"] = is_required
        if is_persistent is not UNSET:
            field_dict["is_persistent"] = is_persistent
        if is_searchable is not UNSET:
            field_dict["is_searchable"] = is_searchable
        if show_in_list_view is not UNSET:
            field_dict["show_in_list_view"] = show_in_list_view
        if show_in_detail_view is not UNSET:
            field_dict["show_in_detail_view"] = show_in_detail_view
        if show_in_mobile_app is not UNSET:
            field_dict["show_in_mobile_app"] = show_in_mobile_app
        if show_in_pod is not UNSET:
            field_dict["show_in_pod"] = show_in_pod
        if show_when_task_type_assignment is not UNSET:
            field_dict["show_when_task_type_assignment"] = show_when_task_type_assignment
        if show_when_task_type_pick_up is not UNSET:
            field_dict["show_when_task_type_pick_up"] = show_when_task_type_pick_up
        if show_when_task_type_drop_off is not UNSET:
            field_dict["show_when_task_type_drop_off"] = show_when_task_type_drop_off
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        ordering = (
            self.ordering if isinstance(self.ordering, Unset) else (None, str(self.ordering).encode(), "text/plain")
        )
        namespace = (
            self.namespace if isinstance(self.namespace, Unset) else (None, str(self.namespace).encode(), "text/plain")
        )
        key = self.key if isinstance(self.key, Unset) else (None, str(self.key).encode(), "text/plain")
        field_name = (
            self.field_name
            if isinstance(self.field_name, Unset)
            else (None, str(self.field_name).encode(), "text/plain")
        )
        value_type: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = (None, str(self.value_type.value).encode(), "text/plain")

        label = self.label if isinstance(self.label, Unset) else (None, str(self.label).encode(), "text/plain")
        choices: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.choices, Unset):
            if self.choices is None:
                choices = None
            else:
                _temp_choices = self.choices
                choices = (None, json.dumps(_temp_choices).encode(), "application/json")

        choices_url = (
            self.choices_url
            if isinstance(self.choices_url, Unset)
            else (None, str(self.choices_url).encode(), "text/plain")
        )
        is_editable = (
            self.is_editable
            if isinstance(self.is_editable, Unset)
            else (None, str(self.is_editable).encode(), "text/plain")
        )
        is_editable_assignee = (
            self.is_editable_assignee
            if isinstance(self.is_editable_assignee, Unset)
            else (None, str(self.is_editable_assignee).encode(), "text/plain")
        )
        is_required = (
            self.is_required
            if isinstance(self.is_required, Unset)
            else (None, str(self.is_required).encode(), "text/plain")
        )
        is_persistent = (
            self.is_persistent
            if isinstance(self.is_persistent, Unset)
            else (None, str(self.is_persistent).encode(), "text/plain")
        )
        is_searchable = (
            self.is_searchable
            if isinstance(self.is_searchable, Unset)
            else (None, str(self.is_searchable).encode(), "text/plain")
        )
        show_in_list_view = (
            self.show_in_list_view
            if isinstance(self.show_in_list_view, Unset)
            else (None, str(self.show_in_list_view).encode(), "text/plain")
        )
        show_in_detail_view = (
            self.show_in_detail_view
            if isinstance(self.show_in_detail_view, Unset)
            else (None, str(self.show_in_detail_view).encode(), "text/plain")
        )
        show_in_mobile_app = (
            self.show_in_mobile_app
            if isinstance(self.show_in_mobile_app, Unset)
            else (None, str(self.show_in_mobile_app).encode(), "text/plain")
        )
        show_in_pod = (
            self.show_in_pod
            if isinstance(self.show_in_pod, Unset)
            else (None, str(self.show_in_pod).encode(), "text/plain")
        )
        show_when_task_type_assignment = (
            self.show_when_task_type_assignment
            if isinstance(self.show_when_task_type_assignment, Unset)
            else (None, str(self.show_when_task_type_assignment).encode(), "text/plain")
        )
        show_when_task_type_pick_up = (
            self.show_when_task_type_pick_up
            if isinstance(self.show_when_task_type_pick_up, Unset)
            else (None, str(self.show_when_task_type_pick_up).encode(), "text/plain")
        )
        show_when_task_type_drop_off = (
            self.show_when_task_type_drop_off
            if isinstance(self.show_when_task_type_drop_off, Unset)
            else (None, str(self.show_when_task_type_drop_off).encode(), "text/plain")
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
        if account is not UNSET:
            field_dict["account"] = account
        if ordering is not UNSET:
            field_dict["ordering"] = ordering
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if key is not UNSET:
            field_dict["key"] = key
        if field_name is not UNSET:
            field_dict["field_name"] = field_name
        if value_type is not UNSET:
            field_dict["value_type"] = value_type
        if label is not UNSET:
            field_dict["label"] = label
        if choices is not UNSET:
            field_dict["choices"] = choices
        if choices_url is not UNSET:
            field_dict["choices_url"] = choices_url
        if is_editable is not UNSET:
            field_dict["is_editable"] = is_editable
        if is_editable_assignee is not UNSET:
            field_dict["is_editable_assignee"] = is_editable_assignee
        if is_required is not UNSET:
            field_dict["is_required"] = is_required
        if is_persistent is not UNSET:
            field_dict["is_persistent"] = is_persistent
        if is_searchable is not UNSET:
            field_dict["is_searchable"] = is_searchable
        if show_in_list_view is not UNSET:
            field_dict["show_in_list_view"] = show_in_list_view
        if show_in_detail_view is not UNSET:
            field_dict["show_in_detail_view"] = show_in_detail_view
        if show_in_mobile_app is not UNSET:
            field_dict["show_in_mobile_app"] = show_in_mobile_app
        if show_in_pod is not UNSET:
            field_dict["show_in_pod"] = show_in_pod
        if show_when_task_type_assignment is not UNSET:
            field_dict["show_when_task_type_assignment"] = show_when_task_type_assignment
        if show_when_task_type_pick_up is not UNSET:
            field_dict["show_when_task_type_pick_up"] = show_when_task_type_pick_up
        if show_when_task_type_drop_off is not UNSET:
            field_dict["show_when_task_type_drop_off"] = show_when_task_type_drop_off
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

        ordering = d.pop("ordering", UNSET)

        namespace = d.pop("namespace", UNSET)

        key = d.pop("key", UNSET)

        field_name = d.pop("field_name", UNSET)

        _value_type = d.pop("value_type", UNSET)
        value_type: Union[Unset, ValueTypeEnum]
        if isinstance(_value_type, Unset):
            value_type = UNSET
        else:
            value_type = ValueTypeEnum(_value_type)

        label = d.pop("label", UNSET)

        choices = cast(List[str], d.pop("choices", UNSET))

        choices_url = d.pop("choices_url", UNSET)

        is_editable = d.pop("is_editable", UNSET)

        is_editable_assignee = d.pop("is_editable_assignee", UNSET)

        is_required = d.pop("is_required", UNSET)

        is_persistent = d.pop("is_persistent", UNSET)

        is_searchable = d.pop("is_searchable", UNSET)

        show_in_list_view = d.pop("show_in_list_view", UNSET)

        show_in_detail_view = d.pop("show_in_detail_view", UNSET)

        show_in_mobile_app = d.pop("show_in_mobile_app", UNSET)

        show_in_pod = d.pop("show_in_pod", UNSET)

        show_when_task_type_assignment = d.pop("show_when_task_type_assignment", UNSET)

        show_when_task_type_pick_up = d.pop("show_when_task_type_pick_up", UNSET)

        show_when_task_type_drop_off = d.pop("show_when_task_type_drop_off", UNSET)

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

        patched_metafield = cls(
            id=id,
            url=url,
            account=account,
            ordering=ordering,
            namespace=namespace,
            key=key,
            field_name=field_name,
            value_type=value_type,
            label=label,
            choices=choices,
            choices_url=choices_url,
            is_editable=is_editable,
            is_editable_assignee=is_editable_assignee,
            is_required=is_required,
            is_persistent=is_persistent,
            is_searchable=is_searchable,
            show_in_list_view=show_in_list_view,
            show_in_detail_view=show_in_detail_view,
            show_in_mobile_app=show_in_mobile_app,
            show_in_pod=show_in_pod,
            show_when_task_type_assignment=show_when_task_type_assignment,
            show_when_task_type_pick_up=show_when_task_type_pick_up,
            show_when_task_type_drop_off=show_when_task_type_drop_off,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_metafield.additional_properties = d
        return patched_metafield

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

import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.active_states_enum import ActiveStatesEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedTracker")


@attr.s(auto_attribs=True)
class PatchedTracker:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        account (Union[Unset, str]):
        tasks (Union[Unset, List[str]]):
        active_from (Union[Unset, None, datetime.datetime]):
        active_until (Union[Unset, None, datetime.datetime]):
        active_states (Union[Unset, List[ActiveStatesEnum]]):
        show_driver_info (Union[Unset, bool]):
        show_destination (Union[Unset, bool]):
        show_eta (Union[Unset, bool]):
        show_sms_action (Union[Unset, bool]):
        show_call_action (Union[Unset, bool]):
        show_logo (Union[Unset, bool]):
        show_path (Union[Unset, bool]):
        autozoom (Union[Unset, bool]):
        max_zoom_level (Union[Unset, None, int]):
        tracking_page_url (Union[Unset, str]):
        reviews_allowed (Union[Unset, bool]):
        reviewed_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    tasks: Union[Unset, List[str]] = UNSET
    active_from: Union[Unset, None, datetime.datetime] = UNSET
    active_until: Union[Unset, None, datetime.datetime] = UNSET
    active_states: Union[Unset, List[ActiveStatesEnum]] = UNSET
    show_driver_info: Union[Unset, bool] = UNSET
    show_destination: Union[Unset, bool] = UNSET
    show_eta: Union[Unset, bool] = UNSET
    show_sms_action: Union[Unset, bool] = UNSET
    show_call_action: Union[Unset, bool] = UNSET
    show_logo: Union[Unset, bool] = UNSET
    show_path: Union[Unset, bool] = UNSET
    autozoom: Union[Unset, bool] = UNSET
    max_zoom_level: Union[Unset, None, int] = UNSET
    tracking_page_url: Union[Unset, str] = UNSET
    reviews_allowed: Union[Unset, bool] = UNSET
    reviewed_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        tasks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = self.tasks

        active_from: Union[Unset, None, str] = UNSET
        if not isinstance(self.active_from, Unset):
            active_from = self.active_from.isoformat() if self.active_from else None

        active_until: Union[Unset, None, str] = UNSET
        if not isinstance(self.active_until, Unset):
            active_until = self.active_until.isoformat() if self.active_until else None

        active_states: Union[Unset, List[str]] = UNSET
        if not isinstance(self.active_states, Unset):
            active_states = []
            for active_states_item_data in self.active_states:
                active_states_item = active_states_item_data.value

                active_states.append(active_states_item)

        show_driver_info = self.show_driver_info
        show_destination = self.show_destination
        show_eta = self.show_eta
        show_sms_action = self.show_sms_action
        show_call_action = self.show_call_action
        show_logo = self.show_logo
        show_path = self.show_path
        autozoom = self.autozoom
        max_zoom_level = self.max_zoom_level
        tracking_page_url = self.tracking_page_url
        reviews_allowed = self.reviews_allowed
        reviewed_at: Union[Unset, str] = UNSET
        if not isinstance(self.reviewed_at, Unset):
            reviewed_at = self.reviewed_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if account is not UNSET:
            field_dict["account"] = account
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if active_from is not UNSET:
            field_dict["active_from"] = active_from
        if active_until is not UNSET:
            field_dict["active_until"] = active_until
        if active_states is not UNSET:
            field_dict["active_states"] = active_states
        if show_driver_info is not UNSET:
            field_dict["show_driver_info"] = show_driver_info
        if show_destination is not UNSET:
            field_dict["show_destination"] = show_destination
        if show_eta is not UNSET:
            field_dict["show_eta"] = show_eta
        if show_sms_action is not UNSET:
            field_dict["show_sms_action"] = show_sms_action
        if show_call_action is not UNSET:
            field_dict["show_call_action"] = show_call_action
        if show_logo is not UNSET:
            field_dict["show_logo"] = show_logo
        if show_path is not UNSET:
            field_dict["show_path"] = show_path
        if autozoom is not UNSET:
            field_dict["autozoom"] = autozoom
        if max_zoom_level is not UNSET:
            field_dict["max_zoom_level"] = max_zoom_level
        if tracking_page_url is not UNSET:
            field_dict["tracking_page_url"] = tracking_page_url
        if reviews_allowed is not UNSET:
            field_dict["reviews_allowed"] = reviews_allowed
        if reviewed_at is not UNSET:
            field_dict["reviewed_at"] = reviewed_at

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        tasks: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tasks, Unset):
            _temp_tasks = self.tasks
            tasks = (None, json.dumps(_temp_tasks).encode(), "application/json")

        active_from: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.active_from, Unset):
            active_from = self.active_from.isoformat().encode() if self.active_from else None

        active_until: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.active_until, Unset):
            active_until = self.active_until.isoformat().encode() if self.active_until else None

        active_states: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.active_states, Unset):
            _temp_active_states = []
            for active_states_item_data in self.active_states:
                active_states_item = active_states_item_data.value

                _temp_active_states.append(active_states_item)
            active_states = (None, json.dumps(_temp_active_states).encode(), "application/json")

        show_driver_info = (
            self.show_driver_info
            if isinstance(self.show_driver_info, Unset)
            else (None, str(self.show_driver_info).encode(), "text/plain")
        )
        show_destination = (
            self.show_destination
            if isinstance(self.show_destination, Unset)
            else (None, str(self.show_destination).encode(), "text/plain")
        )
        show_eta = (
            self.show_eta if isinstance(self.show_eta, Unset) else (None, str(self.show_eta).encode(), "text/plain")
        )
        show_sms_action = (
            self.show_sms_action
            if isinstance(self.show_sms_action, Unset)
            else (None, str(self.show_sms_action).encode(), "text/plain")
        )
        show_call_action = (
            self.show_call_action
            if isinstance(self.show_call_action, Unset)
            else (None, str(self.show_call_action).encode(), "text/plain")
        )
        show_logo = (
            self.show_logo if isinstance(self.show_logo, Unset) else (None, str(self.show_logo).encode(), "text/plain")
        )
        show_path = (
            self.show_path if isinstance(self.show_path, Unset) else (None, str(self.show_path).encode(), "text/plain")
        )
        autozoom = (
            self.autozoom if isinstance(self.autozoom, Unset) else (None, str(self.autozoom).encode(), "text/plain")
        )
        max_zoom_level = (
            self.max_zoom_level
            if isinstance(self.max_zoom_level, Unset)
            else (None, str(self.max_zoom_level).encode(), "text/plain")
        )
        tracking_page_url = (
            self.tracking_page_url
            if isinstance(self.tracking_page_url, Unset)
            else (None, str(self.tracking_page_url).encode(), "text/plain")
        )
        reviews_allowed = (
            self.reviews_allowed
            if isinstance(self.reviews_allowed, Unset)
            else (None, str(self.reviews_allowed).encode(), "text/plain")
        )
        reviewed_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.reviewed_at, Unset):
            reviewed_at = self.reviewed_at.isoformat().encode()

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
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if active_from is not UNSET:
            field_dict["active_from"] = active_from
        if active_until is not UNSET:
            field_dict["active_until"] = active_until
        if active_states is not UNSET:
            field_dict["active_states"] = active_states
        if show_driver_info is not UNSET:
            field_dict["show_driver_info"] = show_driver_info
        if show_destination is not UNSET:
            field_dict["show_destination"] = show_destination
        if show_eta is not UNSET:
            field_dict["show_eta"] = show_eta
        if show_sms_action is not UNSET:
            field_dict["show_sms_action"] = show_sms_action
        if show_call_action is not UNSET:
            field_dict["show_call_action"] = show_call_action
        if show_logo is not UNSET:
            field_dict["show_logo"] = show_logo
        if show_path is not UNSET:
            field_dict["show_path"] = show_path
        if autozoom is not UNSET:
            field_dict["autozoom"] = autozoom
        if max_zoom_level is not UNSET:
            field_dict["max_zoom_level"] = max_zoom_level
        if tracking_page_url is not UNSET:
            field_dict["tracking_page_url"] = tracking_page_url
        if reviews_allowed is not UNSET:
            field_dict["reviews_allowed"] = reviews_allowed
        if reviewed_at is not UNSET:
            field_dict["reviewed_at"] = reviewed_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        account = d.pop("account", UNSET)

        tasks = cast(List[str], d.pop("tasks", UNSET))

        _active_from = d.pop("active_from", UNSET)
        active_from: Union[Unset, None, datetime.datetime]
        if _active_from is None:
            active_from = None
        elif isinstance(_active_from, Unset):
            active_from = UNSET
        else:
            active_from = isoparse(_active_from)

        _active_until = d.pop("active_until", UNSET)
        active_until: Union[Unset, None, datetime.datetime]
        if _active_until is None:
            active_until = None
        elif isinstance(_active_until, Unset):
            active_until = UNSET
        else:
            active_until = isoparse(_active_until)

        active_states = []
        _active_states = d.pop("active_states", UNSET)
        for active_states_item_data in _active_states or []:
            active_states_item = ActiveStatesEnum(active_states_item_data)

            active_states.append(active_states_item)

        show_driver_info = d.pop("show_driver_info", UNSET)

        show_destination = d.pop("show_destination", UNSET)

        show_eta = d.pop("show_eta", UNSET)

        show_sms_action = d.pop("show_sms_action", UNSET)

        show_call_action = d.pop("show_call_action", UNSET)

        show_logo = d.pop("show_logo", UNSET)

        show_path = d.pop("show_path", UNSET)

        autozoom = d.pop("autozoom", UNSET)

        max_zoom_level = d.pop("max_zoom_level", UNSET)

        tracking_page_url = d.pop("tracking_page_url", UNSET)

        reviews_allowed = d.pop("reviews_allowed", UNSET)

        _reviewed_at = d.pop("reviewed_at", UNSET)
        reviewed_at: Union[Unset, datetime.datetime]
        if isinstance(_reviewed_at, Unset):
            reviewed_at = UNSET
        else:
            reviewed_at = isoparse(_reviewed_at)

        patched_tracker = cls(
            id=id,
            url=url,
            account=account,
            tasks=tasks,
            active_from=active_from,
            active_until=active_until,
            active_states=active_states,
            show_driver_info=show_driver_info,
            show_destination=show_destination,
            show_eta=show_eta,
            show_sms_action=show_sms_action,
            show_call_action=show_call_action,
            show_logo=show_logo,
            show_path=show_path,
            autozoom=autozoom,
            max_zoom_level=max_zoom_level,
            tracking_page_url=tracking_page_url,
            reviews_allowed=reviews_allowed,
            reviewed_at=reviewed_at,
        )

        patched_tracker.additional_properties = d
        return patched_tracker

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

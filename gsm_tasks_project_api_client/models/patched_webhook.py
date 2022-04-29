import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.patched_webhook_headers import PatchedWebhookHeaders
from ..models.version_enum import VersionEnum
from ..models.webhook_state_enum import WebhookStateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedWebhook")


@attr.s(auto_attribs=True)
class PatchedWebhook:
    """
    Attributes:
        id (Union[Unset, str]):
        url (Union[Unset, str]):
        account (Union[Unset, str]):
        name (Union[Unset, str]):
        version (Union[Unset, VersionEnum]):
        state (Union[Unset, WebhookStateEnum]):
        headers (Union[Unset, PatchedWebhookHeaders]):
        target (Union[Unset, str]):
        task_events (Union[Unset, bool]):
        document_events (Union[Unset, bool]):
        signature_events (Union[Unset, bool]):
        review_events (Union[Unset, bool]):
        notification_emails (Union[Unset, List[str]]):
        failure_count (Union[Unset, int]):
        disable_message (Union[Unset, str]):
        shared_secret (Union[Unset, str]):
        activated_at (Union[Unset, datetime.datetime]):
        disabled_at (Union[Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    version: Union[Unset, VersionEnum] = UNSET
    state: Union[Unset, WebhookStateEnum] = UNSET
    headers: Union[Unset, PatchedWebhookHeaders] = UNSET
    target: Union[Unset, str] = UNSET
    task_events: Union[Unset, bool] = UNSET
    document_events: Union[Unset, bool] = UNSET
    signature_events: Union[Unset, bool] = UNSET
    review_events: Union[Unset, bool] = UNSET
    notification_emails: Union[Unset, List[str]] = UNSET
    failure_count: Union[Unset, int] = UNSET
    disable_message: Union[Unset, str] = UNSET
    shared_secret: Union[Unset, str] = UNSET
    activated_at: Union[Unset, datetime.datetime] = UNSET
    disabled_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        name = self.name
        version: Union[Unset, str] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        target = self.target
        task_events = self.task_events
        document_events = self.document_events
        signature_events = self.signature_events
        review_events = self.review_events
        notification_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.notification_emails, Unset):
            notification_emails = self.notification_emails

        failure_count = self.failure_count
        disable_message = self.disable_message
        shared_secret = self.shared_secret
        activated_at: Union[Unset, str] = UNSET
        if not isinstance(self.activated_at, Unset):
            activated_at = self.activated_at.isoformat()

        disabled_at: Union[Unset, str] = UNSET
        if not isinstance(self.disabled_at, Unset):
            disabled_at = self.disabled_at.isoformat()

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
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if state is not UNSET:
            field_dict["state"] = state
        if headers is not UNSET:
            field_dict["headers"] = headers
        if target is not UNSET:
            field_dict["target"] = target
        if task_events is not UNSET:
            field_dict["task_events"] = task_events
        if document_events is not UNSET:
            field_dict["document_events"] = document_events
        if signature_events is not UNSET:
            field_dict["signature_events"] = signature_events
        if review_events is not UNSET:
            field_dict["review_events"] = review_events
        if notification_emails is not UNSET:
            field_dict["notification_emails"] = notification_emails
        if failure_count is not UNSET:
            field_dict["failure_count"] = failure_count
        if disable_message is not UNSET:
            field_dict["disable_message"] = disable_message
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret
        if activated_at is not UNSET:
            field_dict["activated_at"] = activated_at
        if disabled_at is not UNSET:
            field_dict["disabled_at"] = disabled_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        version: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.version, Unset):
            version = (None, str(self.version.value).encode(), "text/plain")

        state: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.state, Unset):
            state = (None, str(self.state.value).encode(), "text/plain")

        headers: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = (None, json.dumps(self.headers.to_dict()).encode(), "application/json")

        target = self.target if isinstance(self.target, Unset) else (None, str(self.target).encode(), "text/plain")
        task_events = (
            self.task_events
            if isinstance(self.task_events, Unset)
            else (None, str(self.task_events).encode(), "text/plain")
        )
        document_events = (
            self.document_events
            if isinstance(self.document_events, Unset)
            else (None, str(self.document_events).encode(), "text/plain")
        )
        signature_events = (
            self.signature_events
            if isinstance(self.signature_events, Unset)
            else (None, str(self.signature_events).encode(), "text/plain")
        )
        review_events = (
            self.review_events
            if isinstance(self.review_events, Unset)
            else (None, str(self.review_events).encode(), "text/plain")
        )
        notification_emails: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.notification_emails, Unset):
            _temp_notification_emails = self.notification_emails
            notification_emails = (None, json.dumps(_temp_notification_emails).encode(), "application/json")

        failure_count = (
            self.failure_count
            if isinstance(self.failure_count, Unset)
            else (None, str(self.failure_count).encode(), "text/plain")
        )
        disable_message = (
            self.disable_message
            if isinstance(self.disable_message, Unset)
            else (None, str(self.disable_message).encode(), "text/plain")
        )
        shared_secret = (
            self.shared_secret
            if isinstance(self.shared_secret, Unset)
            else (None, str(self.shared_secret).encode(), "text/plain")
        )
        activated_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.activated_at, Unset):
            activated_at = self.activated_at.isoformat().encode()

        disabled_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.disabled_at, Unset):
            disabled_at = self.disabled_at.isoformat().encode()

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
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if state is not UNSET:
            field_dict["state"] = state
        if headers is not UNSET:
            field_dict["headers"] = headers
        if target is not UNSET:
            field_dict["target"] = target
        if task_events is not UNSET:
            field_dict["task_events"] = task_events
        if document_events is not UNSET:
            field_dict["document_events"] = document_events
        if signature_events is not UNSET:
            field_dict["signature_events"] = signature_events
        if review_events is not UNSET:
            field_dict["review_events"] = review_events
        if notification_emails is not UNSET:
            field_dict["notification_emails"] = notification_emails
        if failure_count is not UNSET:
            field_dict["failure_count"] = failure_count
        if disable_message is not UNSET:
            field_dict["disable_message"] = disable_message
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret
        if activated_at is not UNSET:
            field_dict["activated_at"] = activated_at
        if disabled_at is not UNSET:
            field_dict["disabled_at"] = disabled_at
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

        name = d.pop("name", UNSET)

        _version = d.pop("version", UNSET)
        version: Union[Unset, VersionEnum]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = VersionEnum(_version)

        _state = d.pop("state", UNSET)
        state: Union[Unset, WebhookStateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = WebhookStateEnum(_state)

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, PatchedWebhookHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = PatchedWebhookHeaders.from_dict(_headers)

        target = d.pop("target", UNSET)

        task_events = d.pop("task_events", UNSET)

        document_events = d.pop("document_events", UNSET)

        signature_events = d.pop("signature_events", UNSET)

        review_events = d.pop("review_events", UNSET)

        notification_emails = cast(List[str], d.pop("notification_emails", UNSET))

        failure_count = d.pop("failure_count", UNSET)

        disable_message = d.pop("disable_message", UNSET)

        shared_secret = d.pop("shared_secret", UNSET)

        _activated_at = d.pop("activated_at", UNSET)
        activated_at: Union[Unset, datetime.datetime]
        if isinstance(_activated_at, Unset):
            activated_at = UNSET
        else:
            activated_at = isoparse(_activated_at)

        _disabled_at = d.pop("disabled_at", UNSET)
        disabled_at: Union[Unset, datetime.datetime]
        if isinstance(_disabled_at, Unset):
            disabled_at = UNSET
        else:
            disabled_at = isoparse(_disabled_at)

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

        patched_webhook = cls(
            id=id,
            url=url,
            account=account,
            name=name,
            version=version,
            state=state,
            headers=headers,
            target=target,
            task_events=task_events,
            document_events=document_events,
            signature_events=signature_events,
            review_events=review_events,
            notification_emails=notification_emails,
            failure_count=failure_count,
            disable_message=disable_message,
            shared_secret=shared_secret,
            activated_at=activated_at,
            disabled_at=disabled_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        patched_webhook.additional_properties = d
        return patched_webhook

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

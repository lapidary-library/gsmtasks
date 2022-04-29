import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.version_enum import VersionEnum
from ..models.webhook_headers import WebhookHeaders
from ..models.webhook_state_enum import WebhookStateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Webhook")


@attr.s(auto_attribs=True)
class Webhook:
    """
    Attributes:
        id (str):
        url (str):
        account (str):
        name (str):
        state (WebhookStateEnum):
        target (str):
        failure_count (int):
        disable_message (str):
        activated_at (datetime.datetime):
        disabled_at (datetime.datetime):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        version (Union[Unset, VersionEnum]):
        headers (Union[Unset, WebhookHeaders]):
        task_events (Union[Unset, bool]):
        document_events (Union[Unset, bool]):
        signature_events (Union[Unset, bool]):
        review_events (Union[Unset, bool]):
        notification_emails (Union[Unset, List[str]]):
        shared_secret (Union[Unset, str]):
    """

    id: str
    url: str
    account: str
    name: str
    state: WebhookStateEnum
    target: str
    failure_count: int
    disable_message: str
    activated_at: datetime.datetime
    disabled_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    version: Union[Unset, VersionEnum] = UNSET
    headers: Union[Unset, WebhookHeaders] = UNSET
    task_events: Union[Unset, bool] = UNSET
    document_events: Union[Unset, bool] = UNSET
    signature_events: Union[Unset, bool] = UNSET
    review_events: Union[Unset, bool] = UNSET
    notification_emails: Union[Unset, List[str]] = UNSET
    shared_secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        account = self.account
        name = self.name
        state = self.state.value

        target = self.target
        failure_count = self.failure_count
        disable_message = self.disable_message
        activated_at = self.activated_at.isoformat()

        disabled_at = self.disabled_at.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        version: Union[Unset, str] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.value

        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        task_events = self.task_events
        document_events = self.document_events
        signature_events = self.signature_events
        review_events = self.review_events
        notification_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.notification_emails, Unset):
            notification_emails = self.notification_emails

        shared_secret = self.shared_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "name": name,
                "state": state,
                "target": target,
                "failure_count": failure_count,
                "disable_message": disable_message,
                "activated_at": activated_at,
                "disabled_at": disabled_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if headers is not UNSET:
            field_dict["headers"] = headers
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
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        account = self.account if isinstance(self.account, Unset) else (None, str(self.account).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        state = (None, str(self.state.value).encode(), "text/plain")

        target = self.target if isinstance(self.target, Unset) else (None, str(self.target).encode(), "text/plain")
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
        activated_at = self.activated_at.isoformat().encode()

        disabled_at = self.disabled_at.isoformat().encode()

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        version: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.version, Unset):
            version = (None, str(self.version.value).encode(), "text/plain")

        headers: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = (None, json.dumps(self.headers.to_dict()).encode(), "application/json")

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

        shared_secret = (
            self.shared_secret
            if isinstance(self.shared_secret, Unset)
            else (None, str(self.shared_secret).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "url": url,
                "account": account,
                "name": name,
                "state": state,
                "target": target,
                "failure_count": failure_count,
                "disable_message": disable_message,
                "activated_at": activated_at,
                "disabled_at": disabled_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if headers is not UNSET:
            field_dict["headers"] = headers
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
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        account = d.pop("account")

        name = d.pop("name")

        state = WebhookStateEnum(d.pop("state"))

        target = d.pop("target")

        failure_count = d.pop("failure_count")

        disable_message = d.pop("disable_message")

        activated_at = isoparse(d.pop("activated_at"))

        disabled_at = isoparse(d.pop("disabled_at"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        _version = d.pop("version", UNSET)
        version: Union[Unset, VersionEnum]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = VersionEnum(_version)

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, WebhookHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = WebhookHeaders.from_dict(_headers)

        task_events = d.pop("task_events", UNSET)

        document_events = d.pop("document_events", UNSET)

        signature_events = d.pop("signature_events", UNSET)

        review_events = d.pop("review_events", UNSET)

        notification_emails = cast(List[str], d.pop("notification_emails", UNSET))

        shared_secret = d.pop("shared_secret", UNSET)

        webhook = cls(
            id=id,
            url=url,
            account=account,
            name=name,
            state=state,
            target=target,
            failure_count=failure_count,
            disable_message=disable_message,
            activated_at=activated_at,
            disabled_at=disabled_at,
            created_at=created_at,
            updated_at=updated_at,
            version=version,
            headers=headers,
            task_events=task_events,
            document_events=document_events,
            signature_events=signature_events,
            review_events=review_events,
            notification_emails=notification_emails,
            shared_secret=shared_secret,
        )

        webhook.additional_properties = d
        return webhook

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

from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.notification import Notification
from ...models.notifications_list_event import NotificationsListEvent
from ...models.notifications_list_format import NotificationsListFormat
from ...models.notifications_list_recipient import NotificationsListRecipient
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, NotificationsListEvent] = UNSET,
    format_: Union[Unset, None, NotificationsListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    recipient: Union[Unset, None, NotificationsListRecipient] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    via_app: Union[Unset, None, str] = UNSET,
    via_email: Union[Unset, None, str] = UNSET,
    via_sms: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/notifications/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["cursor"] = cursor

    json_event: Union[Unset, None, str] = UNSET
    if not isinstance(event, Unset):
        json_event = event.value if event else None

    params["event"] = json_event

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["ordering"] = ordering

    params["page_size"] = page_size

    json_recipient: Union[Unset, None, str] = UNSET
    if not isinstance(recipient, Unset):
        json_recipient = recipient.value if recipient else None

    params["recipient"] = json_recipient

    params["search"] = search

    params["task"] = task

    params["via_app"] = via_app

    params["via_email"] = via_email

    params["via_sms"] = via_sms

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Notification]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_notification_list_item_data in _response_200:
            componentsschemas_paginated_notification_list_item = Notification.from_dict(
                componentsschemas_paginated_notification_list_item_data
            )

            response_200.append(componentsschemas_paginated_notification_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Notification]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, NotificationsListEvent] = UNSET,
    format_: Union[Unset, None, NotificationsListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    recipient: Union[Unset, None, NotificationsListRecipient] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    via_app: Union[Unset, None, str] = UNSET,
    via_email: Union[Unset, None, str] = UNSET,
    via_sms: Union[Unset, None, str] = UNSET,
) -> Response[List[Notification]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, NotificationsListEvent]):
        format_ (Union[Unset, None, NotificationsListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        recipient (Union[Unset, None, NotificationsListRecipient]):
        search (Union[Unset, None, str]):
        task (Union[Unset, None, str]):
        via_app (Union[Unset, None, str]):
        via_email (Union[Unset, None, str]):
        via_sms (Union[Unset, None, str]):

    Returns:
        Response[List[Notification]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        event=event,
        format_=format_,
        ordering=ordering,
        page_size=page_size,
        recipient=recipient,
        search=search,
        task=task,
        via_app=via_app,
        via_email=via_email,
        via_sms=via_sms,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, NotificationsListEvent] = UNSET,
    format_: Union[Unset, None, NotificationsListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    recipient: Union[Unset, None, NotificationsListRecipient] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    via_app: Union[Unset, None, str] = UNSET,
    via_email: Union[Unset, None, str] = UNSET,
    via_sms: Union[Unset, None, str] = UNSET,
) -> Optional[List[Notification]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, NotificationsListEvent]):
        format_ (Union[Unset, None, NotificationsListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        recipient (Union[Unset, None, NotificationsListRecipient]):
        search (Union[Unset, None, str]):
        task (Union[Unset, None, str]):
        via_app (Union[Unset, None, str]):
        via_email (Union[Unset, None, str]):
        via_sms (Union[Unset, None, str]):

    Returns:
        Response[List[Notification]]
    """

    return sync_detailed(
        client=client,
        account=account,
        cursor=cursor,
        event=event,
        format_=format_,
        ordering=ordering,
        page_size=page_size,
        recipient=recipient,
        search=search,
        task=task,
        via_app=via_app,
        via_email=via_email,
        via_sms=via_sms,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, NotificationsListEvent] = UNSET,
    format_: Union[Unset, None, NotificationsListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    recipient: Union[Unset, None, NotificationsListRecipient] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    via_app: Union[Unset, None, str] = UNSET,
    via_email: Union[Unset, None, str] = UNSET,
    via_sms: Union[Unset, None, str] = UNSET,
) -> Response[List[Notification]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, NotificationsListEvent]):
        format_ (Union[Unset, None, NotificationsListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        recipient (Union[Unset, None, NotificationsListRecipient]):
        search (Union[Unset, None, str]):
        task (Union[Unset, None, str]):
        via_app (Union[Unset, None, str]):
        via_email (Union[Unset, None, str]):
        via_sms (Union[Unset, None, str]):

    Returns:
        Response[List[Notification]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        event=event,
        format_=format_,
        ordering=ordering,
        page_size=page_size,
        recipient=recipient,
        search=search,
        task=task,
        via_app=via_app,
        via_email=via_email,
        via_sms=via_sms,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, NotificationsListEvent] = UNSET,
    format_: Union[Unset, None, NotificationsListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    recipient: Union[Unset, None, NotificationsListRecipient] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    via_app: Union[Unset, None, str] = UNSET,
    via_email: Union[Unset, None, str] = UNSET,
    via_sms: Union[Unset, None, str] = UNSET,
) -> Optional[List[Notification]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, NotificationsListEvent]):
        format_ (Union[Unset, None, NotificationsListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        recipient (Union[Unset, None, NotificationsListRecipient]):
        search (Union[Unset, None, str]):
        task (Union[Unset, None, str]):
        via_app (Union[Unset, None, str]):
        via_email (Union[Unset, None, str]):
        via_sms (Union[Unset, None, str]):

    Returns:
        Response[List[Notification]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            cursor=cursor,
            event=event,
            format_=format_,
            ordering=ordering,
            page_size=page_size,
            recipient=recipient,
            search=search,
            task=task,
            via_app=via_app,
            via_email=via_email,
            via_sms=via_sms,
        )
    ).parsed

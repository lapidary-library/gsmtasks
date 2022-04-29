from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.push_notification import PushNotification
from ...models.push_notifications_list_event import PushNotificationsListEvent
from ...models.push_notifications_list_format import PushNotificationsListFormat
from ...models.push_notifications_list_state import PushNotificationsListState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, PushNotificationsListEvent] = UNSET,
    event_in: Union[Unset, None, str] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, PushNotificationsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, PushNotificationsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    subject_icontains: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/push_notifications/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["cursor"] = cursor

    json_event: Union[Unset, None, str] = UNSET
    if not isinstance(event, Unset):
        json_event = event.value if event else None

    params["event"] = json_event

    params["event__in"] = event_in

    params["external_id"] = external_id

    params["external_id__icontains"] = external_id_icontains

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["id"] = id

    params["message"] = message

    params["message__icontains"] = message_icontains

    params["ordering"] = ordering

    params["page_size"] = page_size

    params["search"] = search

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params["state__in"] = state_in

    params["subject"] = subject

    params["subject__icontains"] = subject_icontains

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[PushNotification]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_push_notification_list_item_data in _response_200:
            componentsschemas_paginated_push_notification_list_item = PushNotification.from_dict(
                componentsschemas_paginated_push_notification_list_item_data
            )

            response_200.append(componentsschemas_paginated_push_notification_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[PushNotification]]:
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
    event: Union[Unset, None, PushNotificationsListEvent] = UNSET,
    event_in: Union[Unset, None, str] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, PushNotificationsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, PushNotificationsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    subject_icontains: Union[Unset, None, str] = UNSET,
) -> Response[List[PushNotification]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, PushNotificationsListEvent]):
        event_in (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        external_id_icontains (Union[Unset, None, str]):
        format_ (Union[Unset, None, PushNotificationsListFormat]):
        id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        message_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, PushNotificationsListState]):
        state_in (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        subject_icontains (Union[Unset, None, str]):

    Returns:
        Response[List[PushNotification]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        event=event,
        event_in=event_in,
        external_id=external_id,
        external_id_icontains=external_id_icontains,
        format_=format_,
        id=id,
        message=message,
        message_icontains=message_icontains,
        ordering=ordering,
        page_size=page_size,
        search=search,
        state=state,
        state_in=state_in,
        subject=subject,
        subject_icontains=subject_icontains,
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
    event: Union[Unset, None, PushNotificationsListEvent] = UNSET,
    event_in: Union[Unset, None, str] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, PushNotificationsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, PushNotificationsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    subject_icontains: Union[Unset, None, str] = UNSET,
) -> Optional[List[PushNotification]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, PushNotificationsListEvent]):
        event_in (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        external_id_icontains (Union[Unset, None, str]):
        format_ (Union[Unset, None, PushNotificationsListFormat]):
        id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        message_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, PushNotificationsListState]):
        state_in (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        subject_icontains (Union[Unset, None, str]):

    Returns:
        Response[List[PushNotification]]
    """

    return sync_detailed(
        client=client,
        account=account,
        cursor=cursor,
        event=event,
        event_in=event_in,
        external_id=external_id,
        external_id_icontains=external_id_icontains,
        format_=format_,
        id=id,
        message=message,
        message_icontains=message_icontains,
        ordering=ordering,
        page_size=page_size,
        search=search,
        state=state,
        state_in=state_in,
        subject=subject,
        subject_icontains=subject_icontains,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, PushNotificationsListEvent] = UNSET,
    event_in: Union[Unset, None, str] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, PushNotificationsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, PushNotificationsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    subject_icontains: Union[Unset, None, str] = UNSET,
) -> Response[List[PushNotification]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, PushNotificationsListEvent]):
        event_in (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        external_id_icontains (Union[Unset, None, str]):
        format_ (Union[Unset, None, PushNotificationsListFormat]):
        id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        message_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, PushNotificationsListState]):
        state_in (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        subject_icontains (Union[Unset, None, str]):

    Returns:
        Response[List[PushNotification]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        event=event,
        event_in=event_in,
        external_id=external_id,
        external_id_icontains=external_id_icontains,
        format_=format_,
        id=id,
        message=message,
        message_icontains=message_icontains,
        ordering=ordering,
        page_size=page_size,
        search=search,
        state=state,
        state_in=state_in,
        subject=subject,
        subject_icontains=subject_icontains,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, PushNotificationsListEvent] = UNSET,
    event_in: Union[Unset, None, str] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, PushNotificationsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, PushNotificationsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    subject_icontains: Union[Unset, None, str] = UNSET,
) -> Optional[List[PushNotification]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, PushNotificationsListEvent]):
        event_in (Union[Unset, None, str]):
        external_id (Union[Unset, None, str]):
        external_id_icontains (Union[Unset, None, str]):
        format_ (Union[Unset, None, PushNotificationsListFormat]):
        id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        message_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, PushNotificationsListState]):
        state_in (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        subject_icontains (Union[Unset, None, str]):

    Returns:
        Response[List[PushNotification]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            cursor=cursor,
            event=event,
            event_in=event_in,
            external_id=external_id,
            external_id_icontains=external_id_icontains,
            format_=format_,
            id=id,
            message=message,
            message_icontains=message_icontains,
            ordering=ordering,
            page_size=page_size,
            search=search,
            state=state,
            state_in=state_in,
            subject=subject,
            subject_icontains=subject_icontains,
        )
    ).parsed

from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.webhook import Webhook
from ...models.webhooks_list_format import WebhooksListFormat
from ...models.webhooks_list_state import WebhooksListState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    document_events: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, WebhooksListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    review_events: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    signature_events: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, WebhooksListState] = UNSET,
    task_events: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/webhooks/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["cursor"] = cursor

    params["document_events"] = document_events

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["ordering"] = ordering

    params["page_size"] = page_size

    params["review_events"] = review_events

    params["search"] = search

    params["signature_events"] = signature_events

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params["task_events"] = task_events

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Webhook]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_webhook_list_item_data in _response_200:
            componentsschemas_paginated_webhook_list_item = Webhook.from_dict(
                componentsschemas_paginated_webhook_list_item_data
            )

            response_200.append(componentsschemas_paginated_webhook_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Webhook]]:
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
    document_events: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, WebhooksListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    review_events: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    signature_events: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, WebhooksListState] = UNSET,
    task_events: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[List[Webhook]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        document_events (Union[Unset, None, str]):
        format_ (Union[Unset, None, WebhooksListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        review_events (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        signature_events (Union[Unset, None, str]):
        state (Union[Unset, None, WebhooksListState]):
        task_events (Union[Unset, None, str]):
        version (Union[Unset, None, str]):

    Returns:
        Response[List[Webhook]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        document_events=document_events,
        format_=format_,
        ordering=ordering,
        page_size=page_size,
        review_events=review_events,
        search=search,
        signature_events=signature_events,
        state=state,
        task_events=task_events,
        version=version,
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
    document_events: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, WebhooksListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    review_events: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    signature_events: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, WebhooksListState] = UNSET,
    task_events: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Optional[List[Webhook]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        document_events (Union[Unset, None, str]):
        format_ (Union[Unset, None, WebhooksListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        review_events (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        signature_events (Union[Unset, None, str]):
        state (Union[Unset, None, WebhooksListState]):
        task_events (Union[Unset, None, str]):
        version (Union[Unset, None, str]):

    Returns:
        Response[List[Webhook]]
    """

    return sync_detailed(
        client=client,
        account=account,
        cursor=cursor,
        document_events=document_events,
        format_=format_,
        ordering=ordering,
        page_size=page_size,
        review_events=review_events,
        search=search,
        signature_events=signature_events,
        state=state,
        task_events=task_events,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    document_events: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, WebhooksListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    review_events: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    signature_events: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, WebhooksListState] = UNSET,
    task_events: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Response[List[Webhook]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        document_events (Union[Unset, None, str]):
        format_ (Union[Unset, None, WebhooksListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        review_events (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        signature_events (Union[Unset, None, str]):
        state (Union[Unset, None, WebhooksListState]):
        task_events (Union[Unset, None, str]):
        version (Union[Unset, None, str]):

    Returns:
        Response[List[Webhook]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        document_events=document_events,
        format_=format_,
        ordering=ordering,
        page_size=page_size,
        review_events=review_events,
        search=search,
        signature_events=signature_events,
        state=state,
        task_events=task_events,
        version=version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    document_events: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, WebhooksListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    review_events: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    signature_events: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, WebhooksListState] = UNSET,
    task_events: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, str] = UNSET,
) -> Optional[List[Webhook]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        document_events (Union[Unset, None, str]):
        format_ (Union[Unset, None, WebhooksListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        review_events (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        signature_events (Union[Unset, None, str]):
        state (Union[Unset, None, WebhooksListState]):
        task_events (Union[Unset, None, str]):
        version (Union[Unset, None, str]):

    Returns:
        Response[List[Webhook]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            cursor=cursor,
            document_events=document_events,
            format_=format_,
            ordering=ordering,
            page_size=page_size,
            review_events=review_events,
            search=search,
            signature_events=signature_events,
            state=state,
            task_events=task_events,
            version=version,
        )
    ).parsed

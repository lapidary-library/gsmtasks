from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.sms import SMS
from ...models.sms_list_format import SmsListFormat
from ...models.sms_list_provider import SmsListProvider
from ...models.sms_list_state import SmsListState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    alphanumeric_sender_id: Union[Unset, None, str] = UNSET,
    alphanumeric_sender_id_icontains: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, SmsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    phone: Union[Unset, None, str] = UNSET,
    phone_icontains: Union[Unset, None, str] = UNSET,
    price: Union[Unset, None, str] = UNSET,
    price_gt: Union[Unset, None, str] = UNSET,
    price_gte: Union[Unset, None, str] = UNSET,
    price_lt: Union[Unset, None, str] = UNSET,
    price_lte: Union[Unset, None, str] = UNSET,
    provider: Union[Unset, None, SmsListProvider] = UNSET,
    provider_in: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    segments_count: Union[Unset, None, str] = UNSET,
    segments_count_gt: Union[Unset, None, str] = UNSET,
    segments_count_gte: Union[Unset, None, str] = UNSET,
    segments_count_lt: Union[Unset, None, str] = UNSET,
    segments_count_lte: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, SmsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/sms/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["alphanumeric_sender_id"] = alphanumeric_sender_id

    params["alphanumeric_sender_id__icontains"] = alphanumeric_sender_id_icontains

    params["cursor"] = cursor

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["id"] = id

    params["message"] = message

    params["message__icontains"] = message_icontains

    params["ordering"] = ordering

    params["page_size"] = page_size

    params["phone"] = phone

    params["phone__icontains"] = phone_icontains

    params["price"] = price

    params["price__gt"] = price_gt

    params["price__gte"] = price_gte

    params["price__lt"] = price_lt

    params["price__lte"] = price_lte

    json_provider: Union[Unset, None, str] = UNSET
    if not isinstance(provider, Unset):
        json_provider = provider.value if provider else None

    params["provider"] = json_provider

    params["provider__in"] = provider_in

    params["search"] = search

    params["segments_count"] = segments_count

    params["segments_count__gt"] = segments_count_gt

    params["segments_count__gte"] = segments_count_gte

    params["segments_count__lt"] = segments_count_lt

    params["segments_count__lte"] = segments_count_lte

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params["state__in"] = state_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[SMS]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_sms_list_item_data in _response_200:
            componentsschemas_paginated_sms_list_item = SMS.from_dict(componentsschemas_paginated_sms_list_item_data)

            response_200.append(componentsschemas_paginated_sms_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[SMS]]:
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
    alphanumeric_sender_id: Union[Unset, None, str] = UNSET,
    alphanumeric_sender_id_icontains: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, SmsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    phone: Union[Unset, None, str] = UNSET,
    phone_icontains: Union[Unset, None, str] = UNSET,
    price: Union[Unset, None, str] = UNSET,
    price_gt: Union[Unset, None, str] = UNSET,
    price_gte: Union[Unset, None, str] = UNSET,
    price_lt: Union[Unset, None, str] = UNSET,
    price_lte: Union[Unset, None, str] = UNSET,
    provider: Union[Unset, None, SmsListProvider] = UNSET,
    provider_in: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    segments_count: Union[Unset, None, str] = UNSET,
    segments_count_gt: Union[Unset, None, str] = UNSET,
    segments_count_gte: Union[Unset, None, str] = UNSET,
    segments_count_lt: Union[Unset, None, str] = UNSET,
    segments_count_lte: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, SmsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
) -> Response[List[SMS]]:
    """
    Args:
        account (Union[Unset, None, str]):
        alphanumeric_sender_id (Union[Unset, None, str]):
        alphanumeric_sender_id_icontains (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, SmsListFormat]):
        id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        message_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        phone (Union[Unset, None, str]):
        phone_icontains (Union[Unset, None, str]):
        price (Union[Unset, None, str]):
        price_gt (Union[Unset, None, str]):
        price_gte (Union[Unset, None, str]):
        price_lt (Union[Unset, None, str]):
        price_lte (Union[Unset, None, str]):
        provider (Union[Unset, None, SmsListProvider]):
        provider_in (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        segments_count (Union[Unset, None, str]):
        segments_count_gt (Union[Unset, None, str]):
        segments_count_gte (Union[Unset, None, str]):
        segments_count_lt (Union[Unset, None, str]):
        segments_count_lte (Union[Unset, None, str]):
        state (Union[Unset, None, SmsListState]):
        state_in (Union[Unset, None, str]):

    Returns:
        Response[List[SMS]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        alphanumeric_sender_id=alphanumeric_sender_id,
        alphanumeric_sender_id_icontains=alphanumeric_sender_id_icontains,
        cursor=cursor,
        format_=format_,
        id=id,
        message=message,
        message_icontains=message_icontains,
        ordering=ordering,
        page_size=page_size,
        phone=phone,
        phone_icontains=phone_icontains,
        price=price,
        price_gt=price_gt,
        price_gte=price_gte,
        price_lt=price_lt,
        price_lte=price_lte,
        provider=provider,
        provider_in=provider_in,
        search=search,
        segments_count=segments_count,
        segments_count_gt=segments_count_gt,
        segments_count_gte=segments_count_gte,
        segments_count_lt=segments_count_lt,
        segments_count_lte=segments_count_lte,
        state=state,
        state_in=state_in,
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
    alphanumeric_sender_id: Union[Unset, None, str] = UNSET,
    alphanumeric_sender_id_icontains: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, SmsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    phone: Union[Unset, None, str] = UNSET,
    phone_icontains: Union[Unset, None, str] = UNSET,
    price: Union[Unset, None, str] = UNSET,
    price_gt: Union[Unset, None, str] = UNSET,
    price_gte: Union[Unset, None, str] = UNSET,
    price_lt: Union[Unset, None, str] = UNSET,
    price_lte: Union[Unset, None, str] = UNSET,
    provider: Union[Unset, None, SmsListProvider] = UNSET,
    provider_in: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    segments_count: Union[Unset, None, str] = UNSET,
    segments_count_gt: Union[Unset, None, str] = UNSET,
    segments_count_gte: Union[Unset, None, str] = UNSET,
    segments_count_lt: Union[Unset, None, str] = UNSET,
    segments_count_lte: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, SmsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
) -> Optional[List[SMS]]:
    """
    Args:
        account (Union[Unset, None, str]):
        alphanumeric_sender_id (Union[Unset, None, str]):
        alphanumeric_sender_id_icontains (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, SmsListFormat]):
        id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        message_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        phone (Union[Unset, None, str]):
        phone_icontains (Union[Unset, None, str]):
        price (Union[Unset, None, str]):
        price_gt (Union[Unset, None, str]):
        price_gte (Union[Unset, None, str]):
        price_lt (Union[Unset, None, str]):
        price_lte (Union[Unset, None, str]):
        provider (Union[Unset, None, SmsListProvider]):
        provider_in (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        segments_count (Union[Unset, None, str]):
        segments_count_gt (Union[Unset, None, str]):
        segments_count_gte (Union[Unset, None, str]):
        segments_count_lt (Union[Unset, None, str]):
        segments_count_lte (Union[Unset, None, str]):
        state (Union[Unset, None, SmsListState]):
        state_in (Union[Unset, None, str]):

    Returns:
        Response[List[SMS]]
    """

    return sync_detailed(
        client=client,
        account=account,
        alphanumeric_sender_id=alphanumeric_sender_id,
        alphanumeric_sender_id_icontains=alphanumeric_sender_id_icontains,
        cursor=cursor,
        format_=format_,
        id=id,
        message=message,
        message_icontains=message_icontains,
        ordering=ordering,
        page_size=page_size,
        phone=phone,
        phone_icontains=phone_icontains,
        price=price,
        price_gt=price_gt,
        price_gte=price_gte,
        price_lt=price_lt,
        price_lte=price_lte,
        provider=provider,
        provider_in=provider_in,
        search=search,
        segments_count=segments_count,
        segments_count_gt=segments_count_gt,
        segments_count_gte=segments_count_gte,
        segments_count_lt=segments_count_lt,
        segments_count_lte=segments_count_lte,
        state=state,
        state_in=state_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    alphanumeric_sender_id: Union[Unset, None, str] = UNSET,
    alphanumeric_sender_id_icontains: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, SmsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    phone: Union[Unset, None, str] = UNSET,
    phone_icontains: Union[Unset, None, str] = UNSET,
    price: Union[Unset, None, str] = UNSET,
    price_gt: Union[Unset, None, str] = UNSET,
    price_gte: Union[Unset, None, str] = UNSET,
    price_lt: Union[Unset, None, str] = UNSET,
    price_lte: Union[Unset, None, str] = UNSET,
    provider: Union[Unset, None, SmsListProvider] = UNSET,
    provider_in: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    segments_count: Union[Unset, None, str] = UNSET,
    segments_count_gt: Union[Unset, None, str] = UNSET,
    segments_count_gte: Union[Unset, None, str] = UNSET,
    segments_count_lt: Union[Unset, None, str] = UNSET,
    segments_count_lte: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, SmsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
) -> Response[List[SMS]]:
    """
    Args:
        account (Union[Unset, None, str]):
        alphanumeric_sender_id (Union[Unset, None, str]):
        alphanumeric_sender_id_icontains (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, SmsListFormat]):
        id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        message_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        phone (Union[Unset, None, str]):
        phone_icontains (Union[Unset, None, str]):
        price (Union[Unset, None, str]):
        price_gt (Union[Unset, None, str]):
        price_gte (Union[Unset, None, str]):
        price_lt (Union[Unset, None, str]):
        price_lte (Union[Unset, None, str]):
        provider (Union[Unset, None, SmsListProvider]):
        provider_in (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        segments_count (Union[Unset, None, str]):
        segments_count_gt (Union[Unset, None, str]):
        segments_count_gte (Union[Unset, None, str]):
        segments_count_lt (Union[Unset, None, str]):
        segments_count_lte (Union[Unset, None, str]):
        state (Union[Unset, None, SmsListState]):
        state_in (Union[Unset, None, str]):

    Returns:
        Response[List[SMS]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        alphanumeric_sender_id=alphanumeric_sender_id,
        alphanumeric_sender_id_icontains=alphanumeric_sender_id_icontains,
        cursor=cursor,
        format_=format_,
        id=id,
        message=message,
        message_icontains=message_icontains,
        ordering=ordering,
        page_size=page_size,
        phone=phone,
        phone_icontains=phone_icontains,
        price=price,
        price_gt=price_gt,
        price_gte=price_gte,
        price_lt=price_lt,
        price_lte=price_lte,
        provider=provider,
        provider_in=provider_in,
        search=search,
        segments_count=segments_count,
        segments_count_gt=segments_count_gt,
        segments_count_gte=segments_count_gte,
        segments_count_lt=segments_count_lt,
        segments_count_lte=segments_count_lte,
        state=state,
        state_in=state_in,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    alphanumeric_sender_id: Union[Unset, None, str] = UNSET,
    alphanumeric_sender_id_icontains: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, SmsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    phone: Union[Unset, None, str] = UNSET,
    phone_icontains: Union[Unset, None, str] = UNSET,
    price: Union[Unset, None, str] = UNSET,
    price_gt: Union[Unset, None, str] = UNSET,
    price_gte: Union[Unset, None, str] = UNSET,
    price_lt: Union[Unset, None, str] = UNSET,
    price_lte: Union[Unset, None, str] = UNSET,
    provider: Union[Unset, None, SmsListProvider] = UNSET,
    provider_in: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    segments_count: Union[Unset, None, str] = UNSET,
    segments_count_gt: Union[Unset, None, str] = UNSET,
    segments_count_gte: Union[Unset, None, str] = UNSET,
    segments_count_lt: Union[Unset, None, str] = UNSET,
    segments_count_lte: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, SmsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
) -> Optional[List[SMS]]:
    """
    Args:
        account (Union[Unset, None, str]):
        alphanumeric_sender_id (Union[Unset, None, str]):
        alphanumeric_sender_id_icontains (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, SmsListFormat]):
        id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        message_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        phone (Union[Unset, None, str]):
        phone_icontains (Union[Unset, None, str]):
        price (Union[Unset, None, str]):
        price_gt (Union[Unset, None, str]):
        price_gte (Union[Unset, None, str]):
        price_lt (Union[Unset, None, str]):
        price_lte (Union[Unset, None, str]):
        provider (Union[Unset, None, SmsListProvider]):
        provider_in (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        segments_count (Union[Unset, None, str]):
        segments_count_gt (Union[Unset, None, str]):
        segments_count_gte (Union[Unset, None, str]):
        segments_count_lt (Union[Unset, None, str]):
        segments_count_lte (Union[Unset, None, str]):
        state (Union[Unset, None, SmsListState]):
        state_in (Union[Unset, None, str]):

    Returns:
        Response[List[SMS]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            alphanumeric_sender_id=alphanumeric_sender_id,
            alphanumeric_sender_id_icontains=alphanumeric_sender_id_icontains,
            cursor=cursor,
            format_=format_,
            id=id,
            message=message,
            message_icontains=message_icontains,
            ordering=ordering,
            page_size=page_size,
            phone=phone,
            phone_icontains=phone_icontains,
            price=price,
            price_gt=price_gt,
            price_gte=price_gte,
            price_lt=price_lt,
            price_lte=price_lte,
            provider=provider,
            provider_in=provider_in,
            search=search,
            segments_count=segments_count,
            segments_count_gt=segments_count_gt,
            segments_count_gte=segments_count_gte,
            segments_count_lt=segments_count_lt,
            segments_count_lte=segments_count_lte,
            state=state,
            state_in=state_in,
        )
    ).parsed

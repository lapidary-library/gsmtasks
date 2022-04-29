from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.recurrence import Recurrence
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/recurrences/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["cursor"] = cursor

    params["order"] = order

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Recurrence]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_recurrence_list_item_data in _response_200:
            componentsschemas_paginated_recurrence_list_item = Recurrence.from_dict(
                componentsschemas_paginated_recurrence_list_item_data
            )

            response_200.append(componentsschemas_paginated_recurrence_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Recurrence]]:
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
    order: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[List[Recurrence]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        order (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[Recurrence]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        order=order,
        page_size=page_size,
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
    order: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[List[Recurrence]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        order (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[Recurrence]]
    """

    return sync_detailed(
        client=client,
        account=account,
        cursor=cursor,
        order=order,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[List[Recurrence]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        order (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[Recurrence]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        order=order,
        page_size=page_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[List[Recurrence]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        order (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[Recurrence]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            cursor=cursor,
            order=order,
            page_size=page_size,
        )
    ).parsed

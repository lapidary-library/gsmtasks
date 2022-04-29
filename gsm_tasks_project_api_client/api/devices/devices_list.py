from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.device import Device
from ...models.devices_list_format import DevicesListFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, DevicesListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
    user_account_roles_account: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/devices/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["cursor"] = cursor

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["page_size"] = page_size

    params["search"] = search

    params["user"] = user

    params["user__account_roles__account"] = user_account_roles_account

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Device]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_device_list_item_data in _response_200:
            componentsschemas_paginated_device_list_item = Device.from_dict(
                componentsschemas_paginated_device_list_item_data
            )

            response_200.append(componentsschemas_paginated_device_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Device]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, DevicesListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
    user_account_roles_account: Union[Unset, None, str] = UNSET,
) -> Response[List[Device]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, DevicesListFormat]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        user (Union[Unset, None, str]):
        user_account_roles_account (Union[Unset, None, str]):

    Returns:
        Response[List[Device]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
        search=search,
        user=user,
        user_account_roles_account=user_account_roles_account,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, DevicesListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
    user_account_roles_account: Union[Unset, None, str] = UNSET,
) -> Optional[List[Device]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, DevicesListFormat]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        user (Union[Unset, None, str]):
        user_account_roles_account (Union[Unset, None, str]):

    Returns:
        Response[List[Device]]
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
        search=search,
        user=user,
        user_account_roles_account=user_account_roles_account,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, DevicesListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
    user_account_roles_account: Union[Unset, None, str] = UNSET,
) -> Response[List[Device]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, DevicesListFormat]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        user (Union[Unset, None, str]):
        user_account_roles_account (Union[Unset, None, str]):

    Returns:
        Response[List[Device]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
        search=search,
        user=user,
        user_account_roles_account=user_account_roles_account,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, DevicesListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
    user_account_roles_account: Union[Unset, None, str] = UNSET,
) -> Optional[List[Device]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, DevicesListFormat]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        user (Union[Unset, None, str]):
        user_account_roles_account (Union[Unset, None, str]):

    Returns:
        Response[List[Device]]
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            format_=format_,
            page_size=page_size,
            search=search,
            user=user,
            user_account_roles_account=user_account_roles_account,
        )
    ).parsed

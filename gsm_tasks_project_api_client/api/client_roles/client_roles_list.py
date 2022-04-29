from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.client_role import ClientRole
from ...models.client_roles_list_format import ClientRolesListFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    client: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ClientRolesListFormat] = UNSET,
    is_active: Union[Unset, None, str] = UNSET,
    is_manager: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/client_roles/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["client"] = client

    params["cursor"] = cursor

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["is_active"] = is_active

    params["is_manager"] = is_manager

    params["page_size"] = page_size

    params["search"] = search

    params["user"] = user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ClientRole]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_client_role_list_item_data in _response_200:
            componentsschemas_paginated_client_role_list_item = ClientRole.from_dict(
                componentsschemas_paginated_client_role_list_item_data
            )

            response_200.append(componentsschemas_paginated_client_role_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ClientRole]]:
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
    client: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ClientRolesListFormat] = UNSET,
    is_active: Union[Unset, None, str] = UNSET,
    is_manager: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Response[List[ClientRole]]:
    """
    Args:
        account (Union[Unset, None, str]):
        client (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ClientRolesListFormat]):
        is_active (Union[Unset, None, str]):
        is_manager (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[ClientRole]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        client=client,
        cursor=cursor,
        format_=format_,
        is_active=is_active,
        is_manager=is_manager,
        page_size=page_size,
        search=search,
        user=user,
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
    client: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ClientRolesListFormat] = UNSET,
    is_active: Union[Unset, None, str] = UNSET,
    is_manager: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Optional[List[ClientRole]]:
    """
    Args:
        account (Union[Unset, None, str]):
        client (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ClientRolesListFormat]):
        is_active (Union[Unset, None, str]):
        is_manager (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[ClientRole]]
    """

    return sync_detailed(
        client=client,
        account=account,
        client=client,
        cursor=cursor,
        format_=format_,
        is_active=is_active,
        is_manager=is_manager,
        page_size=page_size,
        search=search,
        user=user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    client: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ClientRolesListFormat] = UNSET,
    is_active: Union[Unset, None, str] = UNSET,
    is_manager: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Response[List[ClientRole]]:
    """
    Args:
        account (Union[Unset, None, str]):
        client (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ClientRolesListFormat]):
        is_active (Union[Unset, None, str]):
        is_manager (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[ClientRole]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        client=client,
        cursor=cursor,
        format_=format_,
        is_active=is_active,
        is_manager=is_manager,
        page_size=page_size,
        search=search,
        user=user,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    client: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ClientRolesListFormat] = UNSET,
    is_active: Union[Unset, None, str] = UNSET,
    is_manager: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Optional[List[ClientRole]]:
    """
    Args:
        account (Union[Unset, None, str]):
        client (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ClientRolesListFormat]):
        is_active (Union[Unset, None, str]):
        is_manager (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[ClientRole]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            client=client,
            cursor=cursor,
            format_=format_,
            is_active=is_active,
            is_manager=is_manager,
            page_size=page_size,
            search=search,
            user=user,
        )
    ).parsed

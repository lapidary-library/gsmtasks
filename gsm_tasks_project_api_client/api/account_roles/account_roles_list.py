from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.account_role import AccountRole
from ...models.account_roles_list_format import AccountRolesListFormat
from ...models.account_roles_list_state import AccountRolesListState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    display_name: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, AccountRolesListFormat] = UNSET,
    is_integration: Union[Unset, None, str] = UNSET,
    is_manager: Union[Unset, None, str] = UNSET,
    is_worker: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, AccountRolesListState] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/account_roles/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["cursor"] = cursor

    params["display_name"] = display_name

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["is_integration"] = is_integration

    params["is_manager"] = is_manager

    params["is_worker"] = is_worker

    params["ordering"] = ordering

    params["page_size"] = page_size

    params["search"] = search

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

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


def _parse_response(*, response: httpx.Response) -> Optional[List[AccountRole]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_account_role_list_item_data in _response_200:
            componentsschemas_paginated_account_role_list_item = AccountRole.from_dict(
                componentsschemas_paginated_account_role_list_item_data
            )

            response_200.append(componentsschemas_paginated_account_role_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[AccountRole]]:
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
    display_name: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, AccountRolesListFormat] = UNSET,
    is_integration: Union[Unset, None, str] = UNSET,
    is_manager: Union[Unset, None, str] = UNSET,
    is_worker: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, AccountRolesListState] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Response[List[AccountRole]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        display_name (Union[Unset, None, str]):
        format_ (Union[Unset, None, AccountRolesListFormat]):
        is_integration (Union[Unset, None, str]):
        is_manager (Union[Unset, None, str]):
        is_worker (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, AccountRolesListState]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[AccountRole]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        display_name=display_name,
        format_=format_,
        is_integration=is_integration,
        is_manager=is_manager,
        is_worker=is_worker,
        ordering=ordering,
        page_size=page_size,
        search=search,
        state=state,
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
    cursor: Union[Unset, None, int] = UNSET,
    display_name: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, AccountRolesListFormat] = UNSET,
    is_integration: Union[Unset, None, str] = UNSET,
    is_manager: Union[Unset, None, str] = UNSET,
    is_worker: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, AccountRolesListState] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Optional[List[AccountRole]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        display_name (Union[Unset, None, str]):
        format_ (Union[Unset, None, AccountRolesListFormat]):
        is_integration (Union[Unset, None, str]):
        is_manager (Union[Unset, None, str]):
        is_worker (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, AccountRolesListState]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[AccountRole]]
    """

    return sync_detailed(
        client=client,
        account=account,
        cursor=cursor,
        display_name=display_name,
        format_=format_,
        is_integration=is_integration,
        is_manager=is_manager,
        is_worker=is_worker,
        ordering=ordering,
        page_size=page_size,
        search=search,
        state=state,
        user=user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    display_name: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, AccountRolesListFormat] = UNSET,
    is_integration: Union[Unset, None, str] = UNSET,
    is_manager: Union[Unset, None, str] = UNSET,
    is_worker: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, AccountRolesListState] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Response[List[AccountRole]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        display_name (Union[Unset, None, str]):
        format_ (Union[Unset, None, AccountRolesListFormat]):
        is_integration (Union[Unset, None, str]):
        is_manager (Union[Unset, None, str]):
        is_worker (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, AccountRolesListState]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[AccountRole]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        display_name=display_name,
        format_=format_,
        is_integration=is_integration,
        is_manager=is_manager,
        is_worker=is_worker,
        ordering=ordering,
        page_size=page_size,
        search=search,
        state=state,
        user=user,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    display_name: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, AccountRolesListFormat] = UNSET,
    is_integration: Union[Unset, None, str] = UNSET,
    is_manager: Union[Unset, None, str] = UNSET,
    is_worker: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, AccountRolesListState] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Optional[List[AccountRole]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        display_name (Union[Unset, None, str]):
        format_ (Union[Unset, None, AccountRolesListFormat]):
        is_integration (Union[Unset, None, str]):
        is_manager (Union[Unset, None, str]):
        is_worker (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, AccountRolesListState]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[AccountRole]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            cursor=cursor,
            display_name=display_name,
            format_=format_,
            is_integration=is_integration,
            is_manager=is_manager,
            is_worker=is_worker,
            ordering=ordering,
            page_size=page_size,
            search=search,
            state=state,
            user=user,
        )
    ).parsed

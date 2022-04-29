from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.users_on_duty_log_list_format import UsersOnDutyLogListFormat
from ...models.users_on_duty_log_list_mode import UsersOnDutyLogListMode
from ...models.users_on_duty_log_list_status import UsersOnDutyLogListStatus
from ...models.working_state import WorkingState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    account_role: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, UsersOnDutyLogListFormat] = UNSET,
    mode: Union[Unset, None, UsersOnDutyLogListMode] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, UsersOnDutyLogListStatus] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/users_on_duty_log/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["account_role"] = account_role

    params["cursor"] = cursor

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    json_mode: Union[Unset, None, str] = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value if mode else None

    params["mode"] = json_mode

    params["ordering"] = ordering

    params["page_size"] = page_size

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

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


def _parse_response(*, response: httpx.Response) -> Optional[List[WorkingState]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_working_state_list_item_data in _response_200:
            componentsschemas_paginated_working_state_list_item = WorkingState.from_dict(
                componentsschemas_paginated_working_state_list_item_data
            )

            response_200.append(componentsschemas_paginated_working_state_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[WorkingState]]:
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
    account_role: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, UsersOnDutyLogListFormat] = UNSET,
    mode: Union[Unset, None, UsersOnDutyLogListMode] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, UsersOnDutyLogListStatus] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Response[List[WorkingState]]:
    """
    Args:
        account (Union[Unset, None, str]):
        account_role (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, UsersOnDutyLogListFormat]):
        mode (Union[Unset, None, UsersOnDutyLogListMode]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        status (Union[Unset, None, UsersOnDutyLogListStatus]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[WorkingState]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        account_role=account_role,
        cursor=cursor,
        format_=format_,
        mode=mode,
        ordering=ordering,
        page_size=page_size,
        status=status,
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
    account_role: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, UsersOnDutyLogListFormat] = UNSET,
    mode: Union[Unset, None, UsersOnDutyLogListMode] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, UsersOnDutyLogListStatus] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Optional[List[WorkingState]]:
    """
    Args:
        account (Union[Unset, None, str]):
        account_role (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, UsersOnDutyLogListFormat]):
        mode (Union[Unset, None, UsersOnDutyLogListMode]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        status (Union[Unset, None, UsersOnDutyLogListStatus]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[WorkingState]]
    """

    return sync_detailed(
        client=client,
        account=account,
        account_role=account_role,
        cursor=cursor,
        format_=format_,
        mode=mode,
        ordering=ordering,
        page_size=page_size,
        status=status,
        user=user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    account_role: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, UsersOnDutyLogListFormat] = UNSET,
    mode: Union[Unset, None, UsersOnDutyLogListMode] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, UsersOnDutyLogListStatus] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Response[List[WorkingState]]:
    """
    Args:
        account (Union[Unset, None, str]):
        account_role (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, UsersOnDutyLogListFormat]):
        mode (Union[Unset, None, UsersOnDutyLogListMode]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        status (Union[Unset, None, UsersOnDutyLogListStatus]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[WorkingState]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        account_role=account_role,
        cursor=cursor,
        format_=format_,
        mode=mode,
        ordering=ordering,
        page_size=page_size,
        status=status,
        user=user,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    account_role: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, UsersOnDutyLogListFormat] = UNSET,
    mode: Union[Unset, None, UsersOnDutyLogListMode] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, UsersOnDutyLogListStatus] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Optional[List[WorkingState]]:
    """
    Args:
        account (Union[Unset, None, str]):
        account_role (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, UsersOnDutyLogListFormat]):
        mode (Union[Unset, None, UsersOnDutyLogListMode]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        status (Union[Unset, None, UsersOnDutyLogListStatus]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[WorkingState]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            account_role=account_role,
            cursor=cursor,
            format_=format_,
            mode=mode,
            ordering=ordering,
            page_size=page_size,
            status=status,
            user=user,
        )
    ).parsed

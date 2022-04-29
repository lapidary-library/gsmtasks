from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.authenticated_user_create import AuthenticatedUserCreate
from ...models.authenticated_user_update import AuthenticatedUserUpdate
from ...models.on_duty import OnDuty
from ...models.readable_user import ReadableUser
from ...models.users_list_format import UsersListFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, UsersListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/users/".format(client.base_url)

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[List[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_user_list_item_data in _response_200:

            def _parse_componentsschemas_paginated_user_list_item(
                data: object,
            ) -> Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_type_0 = OnDuty.from_dict(data)

                    return componentsschemas_user_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_type_1 = AuthenticatedUserCreate.from_dict(data)

                    return componentsschemas_user_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_type_2 = AuthenticatedUserUpdate.from_dict(data)

                    return componentsschemas_user_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_type_3 = ReadableUser.from_dict(data)

                return componentsschemas_user_type_3

            componentsschemas_paginated_user_list_item = _parse_componentsschemas_paginated_user_list_item(
                componentsschemas_paginated_user_list_item_data
            )

            response_200.append(componentsschemas_paginated_user_list_item)

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[List[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]]:
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
    format_: Union[Unset, None, UsersListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[List[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, UsersListFormat]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
        search=search,
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
    format_: Union[Unset, None, UsersListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[List[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, UsersListFormat]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]]
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, UsersListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[List[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, UsersListFormat]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
        search=search,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, UsersListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[List[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, UsersListFormat]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            format_=format_,
            page_size=page_size,
            search=search,
        )
    ).parsed

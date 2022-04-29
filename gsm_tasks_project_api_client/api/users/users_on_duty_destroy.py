from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.authenticated_user_create import AuthenticatedUserCreate
from ...models.authenticated_user_update import AuthenticatedUserUpdate
from ...models.on_duty import OnDuty
from ...models.readable_user import ReadableUser
from ...models.users_on_duty_destroy_format import UsersOnDutyDestroyFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, UsersOnDutyDestroyFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/users/{id}/on_duty/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]:
    if response.status_code == 200:

        def _parse_response_200(
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

        response_200 = _parse_response_200(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, UsersOnDutyDestroyFormat] = UNSET,
) -> Response[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, UsersOnDutyDestroyFormat]):

    Returns:
        Response[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        format_=format_,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, UsersOnDutyDestroyFormat] = UNSET,
) -> Optional[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, UsersOnDutyDestroyFormat]):

    Returns:
        Response[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]
    """

    return sync_detailed(
        id=id,
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, UsersOnDutyDestroyFormat] = UNSET,
) -> Response[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, UsersOnDutyDestroyFormat]):

    Returns:
        Response[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, UsersOnDutyDestroyFormat] = UNSET,
) -> Optional[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, UsersOnDutyDestroyFormat]):

    Returns:
        Response[Union[AuthenticatedUserCreate, AuthenticatedUserUpdate, OnDuty, ReadableUser]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            format_=format_,
        )
    ).parsed

from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.account_role import AccountRole
from ...models.account_roles_partial_update_format import AccountRolesPartialUpdateFormat
from ...models.patched_account_role import PatchedAccountRole
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: PatchedAccountRole,
    format_: Union[Unset, None, AccountRolesPartialUpdateFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/account_roles/{id}/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AccountRole]:
    if response.status_code == 200:
        response_200 = AccountRole.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AccountRole]:
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
    json_body: PatchedAccountRole,
    format_: Union[Unset, None, AccountRolesPartialUpdateFormat] = UNSET,
) -> Response[AccountRole]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, AccountRolesPartialUpdateFormat]):
        json_body (PatchedAccountRole):

    Returns:
        Response[AccountRole]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
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
    json_body: PatchedAccountRole,
    format_: Union[Unset, None, AccountRolesPartialUpdateFormat] = UNSET,
) -> Optional[AccountRole]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, AccountRolesPartialUpdateFormat]):
        json_body (PatchedAccountRole):

    Returns:
        Response[AccountRole]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: PatchedAccountRole,
    format_: Union[Unset, None, AccountRolesPartialUpdateFormat] = UNSET,
) -> Response[AccountRole]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, AccountRolesPartialUpdateFormat]):
        json_body (PatchedAccountRole):

    Returns:
        Response[AccountRole]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: PatchedAccountRole,
    format_: Union[Unset, None, AccountRolesPartialUpdateFormat] = UNSET,
) -> Optional[AccountRole]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, AccountRolesPartialUpdateFormat]):
        json_body (PatchedAccountRole):

    Returns:
        Response[AccountRole]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            format_=format_,
        )
    ).parsed

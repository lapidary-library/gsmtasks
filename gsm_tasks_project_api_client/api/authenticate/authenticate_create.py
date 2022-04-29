from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.auth_token import AuthToken
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    form_data: AuthToken,
    multipart_data: AuthToken,
    json_body: AuthToken,
) -> Dict[str, Any]:
    url = "{}/authenticate/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[AuthToken]:
    if response.status_code == 200:
        response_200 = AuthToken.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AuthToken]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    form_data: AuthToken,
    multipart_data: AuthToken,
    json_body: AuthToken,
) -> Response[AuthToken]:
    """
    Args:
        multipart_data (AuthToken):
        json_body (AuthToken):

    Returns:
        Response[AuthToken]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    form_data: AuthToken,
    multipart_data: AuthToken,
    json_body: AuthToken,
) -> Optional[AuthToken]:
    """
    Args:
        multipart_data (AuthToken):
        json_body (AuthToken):

    Returns:
        Response[AuthToken]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    form_data: AuthToken,
    multipart_data: AuthToken,
    json_body: AuthToken,
) -> Response[AuthToken]:
    """
    Args:
        multipart_data (AuthToken):
        json_body (AuthToken):

    Returns:
        Response[AuthToken]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    form_data: AuthToken,
    multipart_data: AuthToken,
    json_body: AuthToken,
) -> Optional[AuthToken]:
    """
    Args:
        multipart_data (AuthToken):
        json_body (AuthToken):

    Returns:
        Response[AuthToken]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed

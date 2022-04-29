from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.password_reset import PasswordReset
from ...models.password_reset_create_format import PasswordResetCreateFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    form_data: PasswordReset,
    multipart_data: PasswordReset,
    json_body: PasswordReset,
    format_: Union[Unset, None, PasswordResetCreateFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/password_reset/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PasswordReset]:
    if response.status_code == 201:
        response_201 = PasswordReset.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[PasswordReset]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    form_data: PasswordReset,
    multipart_data: PasswordReset,
    json_body: PasswordReset,
    format_: Union[Unset, None, PasswordResetCreateFormat] = UNSET,
) -> Response[PasswordReset]:
    """
    Args:
        format_ (Union[Unset, None, PasswordResetCreateFormat]):
        multipart_data (PasswordReset):
        json_body (PasswordReset):

    Returns:
        Response[PasswordReset]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    form_data: PasswordReset,
    multipart_data: PasswordReset,
    json_body: PasswordReset,
    format_: Union[Unset, None, PasswordResetCreateFormat] = UNSET,
) -> Optional[PasswordReset]:
    """
    Args:
        format_ (Union[Unset, None, PasswordResetCreateFormat]):
        multipart_data (PasswordReset):
        json_body (PasswordReset):

    Returns:
        Response[PasswordReset]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    form_data: PasswordReset,
    multipart_data: PasswordReset,
    json_body: PasswordReset,
    format_: Union[Unset, None, PasswordResetCreateFormat] = UNSET,
) -> Response[PasswordReset]:
    """
    Args:
        format_ (Union[Unset, None, PasswordResetCreateFormat]):
        multipart_data (PasswordReset):
        json_body (PasswordReset):

    Returns:
        Response[PasswordReset]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    form_data: PasswordReset,
    multipart_data: PasswordReset,
    json_body: PasswordReset,
    format_: Union[Unset, None, PasswordResetCreateFormat] = UNSET,
) -> Optional[PasswordReset]:
    """
    Args:
        format_ (Union[Unset, None, PasswordResetCreateFormat]):
        multipart_data (PasswordReset):
        json_body (PasswordReset):

    Returns:
        Response[PasswordReset]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
            format_=format_,
        )
    ).parsed

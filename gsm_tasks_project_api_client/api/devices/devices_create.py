from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.device import Device
from ...models.devices_create_format import DevicesCreateFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: Device,
    multipart_data: Device,
    json_body: Device,
    format_: Union[Unset, None, DevicesCreateFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/devices/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Device]:
    if response.status_code == 201:
        response_201 = Device.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[Device]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: Device,
    multipart_data: Device,
    json_body: Device,
    format_: Union[Unset, None, DevicesCreateFormat] = UNSET,
) -> Response[Device]:
    """
    Args:
        format_ (Union[Unset, None, DevicesCreateFormat]):
        multipart_data (Device):
        json_body (Device):

    Returns:
        Response[Device]
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
    client: AuthenticatedClient,
    form_data: Device,
    multipart_data: Device,
    json_body: Device,
    format_: Union[Unset, None, DevicesCreateFormat] = UNSET,
) -> Optional[Device]:
    """
    Args:
        format_ (Union[Unset, None, DevicesCreateFormat]):
        multipart_data (Device):
        json_body (Device):

    Returns:
        Response[Device]
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
    client: AuthenticatedClient,
    form_data: Device,
    multipart_data: Device,
    json_body: Device,
    format_: Union[Unset, None, DevicesCreateFormat] = UNSET,
) -> Response[Device]:
    """
    Args:
        format_ (Union[Unset, None, DevicesCreateFormat]):
        multipart_data (Device):
        json_body (Device):

    Returns:
        Response[Device]
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
    client: AuthenticatedClient,
    form_data: Device,
    multipart_data: Device,
    json_body: Device,
    format_: Union[Unset, None, DevicesCreateFormat] = UNSET,
) -> Optional[Device]:
    """
    Args:
        format_ (Union[Unset, None, DevicesCreateFormat]):
        multipart_data (Device):
        json_body (Device):

    Returns:
        Response[Device]
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

from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.order_serializer_v2 import OrderSerializerV2
from ...models.patched_order_serializer_v2 import PatchedOrderSerializerV2
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedOrderSerializerV2,
    multipart_data: PatchedOrderSerializerV2,
    json_body: PatchedOrderSerializerV2,
) -> Dict[str, Any]:
    url = "{}/orders/{id}/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[OrderSerializerV2]:
    if response.status_code == 200:
        response_200 = OrderSerializerV2.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[OrderSerializerV2]:
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
    form_data: PatchedOrderSerializerV2,
    multipart_data: PatchedOrderSerializerV2,
    json_body: PatchedOrderSerializerV2,
) -> Response[OrderSerializerV2]:
    """
    Args:
        id (str):
        multipart_data (PatchedOrderSerializerV2):
        json_body (PatchedOrderSerializerV2):

    Returns:
        Response[OrderSerializerV2]
    """

    kwargs = _get_kwargs(
        id=id,
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
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedOrderSerializerV2,
    multipart_data: PatchedOrderSerializerV2,
    json_body: PatchedOrderSerializerV2,
) -> Optional[OrderSerializerV2]:
    """
    Args:
        id (str):
        multipart_data (PatchedOrderSerializerV2):
        json_body (PatchedOrderSerializerV2):

    Returns:
        Response[OrderSerializerV2]
    """

    return sync_detailed(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedOrderSerializerV2,
    multipart_data: PatchedOrderSerializerV2,
    json_body: PatchedOrderSerializerV2,
) -> Response[OrderSerializerV2]:
    """
    Args:
        id (str):
        multipart_data (PatchedOrderSerializerV2):
        json_body (PatchedOrderSerializerV2):

    Returns:
        Response[OrderSerializerV2]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedOrderSerializerV2,
    multipart_data: PatchedOrderSerializerV2,
    json_body: PatchedOrderSerializerV2,
) -> Optional[OrderSerializerV2]:
    """
    Args:
        id (str):
        multipart_data (PatchedOrderSerializerV2):
        json_body (PatchedOrderSerializerV2):

    Returns:
        Response[OrderSerializerV2]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed

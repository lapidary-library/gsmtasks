from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.order_serializer_v2 import OrderSerializerV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    reference: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/orders/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["cursor"] = cursor

    params["external_id"] = external_id

    params["id"] = id

    params["ordering"] = ordering

    params["page_size"] = page_size

    params["reference"] = reference

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


def _parse_response(*, response: httpx.Response) -> Optional[List[OrderSerializerV2]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_order_serializer_v2_list_item_data in _response_200:
            componentsschemas_paginated_order_serializer_v2_list_item = OrderSerializerV2.from_dict(
                componentsschemas_paginated_order_serializer_v2_list_item_data
            )

            response_200.append(componentsschemas_paginated_order_serializer_v2_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[OrderSerializerV2]]:
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
    external_id: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    reference: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[List[OrderSerializerV2]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        external_id (Union[Unset, None, str]):
        id (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        reference (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[OrderSerializerV2]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        external_id=external_id,
        id=id,
        ordering=ordering,
        page_size=page_size,
        reference=reference,
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
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    reference: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[List[OrderSerializerV2]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        external_id (Union[Unset, None, str]):
        id (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        reference (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[OrderSerializerV2]]
    """

    return sync_detailed(
        client=client,
        account=account,
        cursor=cursor,
        external_id=external_id,
        id=id,
        ordering=ordering,
        page_size=page_size,
        reference=reference,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    reference: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[List[OrderSerializerV2]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        external_id (Union[Unset, None, str]):
        id (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        reference (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[OrderSerializerV2]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        external_id=external_id,
        id=id,
        ordering=ordering,
        page_size=page_size,
        reference=reference,
        search=search,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    reference: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[List[OrderSerializerV2]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        external_id (Union[Unset, None, str]):
        id (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        reference (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[OrderSerializerV2]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            cursor=cursor,
            external_id=external_id,
            id=id,
            ordering=ordering,
            page_size=page_size,
            reference=reference,
            search=search,
        )
    ).parsed

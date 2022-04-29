from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.signature import Signature
from ...models.signatures_list_format import SignaturesListFormat
from ...models.signatures_list_source import SignaturesListSource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, SignaturesListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, SignaturesListSource] = UNSET,
    task: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/signatures/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["cursor"] = cursor

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["ordering"] = ordering

    params["page_size"] = page_size

    params["search"] = search

    json_source: Union[Unset, None, str] = UNSET
    if not isinstance(source, Unset):
        json_source = source.value if source else None

    params["source"] = json_source

    params["task"] = task

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Signature]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_signature_list_item_data in _response_200:
            componentsschemas_paginated_signature_list_item = Signature.from_dict(
                componentsschemas_paginated_signature_list_item_data
            )

            response_200.append(componentsschemas_paginated_signature_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Signature]]:
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
    format_: Union[Unset, None, SignaturesListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, SignaturesListSource] = UNSET,
    task: Union[Unset, None, str] = UNSET,
) -> Response[List[Signature]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, SignaturesListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        source (Union[Unset, None, SignaturesListSource]):
        task (Union[Unset, None, str]):

    Returns:
        Response[List[Signature]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        format_=format_,
        ordering=ordering,
        page_size=page_size,
        search=search,
        source=source,
        task=task,
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
    format_: Union[Unset, None, SignaturesListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, SignaturesListSource] = UNSET,
    task: Union[Unset, None, str] = UNSET,
) -> Optional[List[Signature]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, SignaturesListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        source (Union[Unset, None, SignaturesListSource]):
        task (Union[Unset, None, str]):

    Returns:
        Response[List[Signature]]
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        format_=format_,
        ordering=ordering,
        page_size=page_size,
        search=search,
        source=source,
        task=task,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, SignaturesListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, SignaturesListSource] = UNSET,
    task: Union[Unset, None, str] = UNSET,
) -> Response[List[Signature]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, SignaturesListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        source (Union[Unset, None, SignaturesListSource]):
        task (Union[Unset, None, str]):

    Returns:
        Response[List[Signature]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        format_=format_,
        ordering=ordering,
        page_size=page_size,
        search=search,
        source=source,
        task=task,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, SignaturesListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, SignaturesListSource] = UNSET,
    task: Union[Unset, None, str] = UNSET,
) -> Optional[List[Signature]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, SignaturesListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        source (Union[Unset, None, SignaturesListSource]):
        task (Union[Unset, None, str]):

    Returns:
        Response[List[Signature]]
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            format_=format_,
            ordering=ordering,
            page_size=page_size,
            search=search,
            source=source,
            task=task,
        )
    ).parsed

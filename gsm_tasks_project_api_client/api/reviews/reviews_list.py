from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.review import Review
from ...models.reviews_list_format import ReviewsListFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ReviewsListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    tracker: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/reviews/".format(client.base_url)

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

    params["tracker"] = tracker

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Review]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_review_list_item_data in _response_200:
            componentsschemas_paginated_review_list_item = Review.from_dict(
                componentsschemas_paginated_review_list_item_data
            )

            response_200.append(componentsschemas_paginated_review_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Review]]:
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
    format_: Union[Unset, None, ReviewsListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    tracker: Union[Unset, None, str] = UNSET,
) -> Response[List[Review]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ReviewsListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        tracker (Union[Unset, None, str]):

    Returns:
        Response[List[Review]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        format_=format_,
        ordering=ordering,
        page_size=page_size,
        tracker=tracker,
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
    format_: Union[Unset, None, ReviewsListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    tracker: Union[Unset, None, str] = UNSET,
) -> Optional[List[Review]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ReviewsListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        tracker (Union[Unset, None, str]):

    Returns:
        Response[List[Review]]
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        format_=format_,
        ordering=ordering,
        page_size=page_size,
        tracker=tracker,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ReviewsListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    tracker: Union[Unset, None, str] = UNSET,
) -> Response[List[Review]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ReviewsListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        tracker (Union[Unset, None, str]):

    Returns:
        Response[List[Review]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        format_=format_,
        ordering=ordering,
        page_size=page_size,
        tracker=tracker,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ReviewsListFormat] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    tracker: Union[Unset, None, str] = UNSET,
) -> Optional[List[Review]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ReviewsListFormat]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        tracker (Union[Unset, None, str]):

    Returns:
        Response[List[Review]]
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            format_=format_,
            ordering=ordering,
            page_size=page_size,
            tracker=tracker,
        )
    ).parsed

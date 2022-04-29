from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.contact_address import ContactAddress
from ...models.contact_addresses_list_format import ContactAddressesListFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    client: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ContactAddressesListFormat] = UNSET,
    is_orderer: Union[Unset, None, str] = UNSET,
    is_receiver: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/contact_addresses/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["client"] = client

    params["cursor"] = cursor

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["is_orderer"] = is_orderer

    params["is_receiver"] = is_receiver

    params["ordering"] = ordering

    params["page_size"] = page_size

    params["search"] = search

    params["source"] = source

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ContactAddress]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_contact_address_list_item_data in _response_200:
            componentsschemas_paginated_contact_address_list_item = ContactAddress.from_dict(
                componentsschemas_paginated_contact_address_list_item_data
            )

            response_200.append(componentsschemas_paginated_contact_address_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ContactAddress]]:
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
    client: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ContactAddressesListFormat] = UNSET,
    is_orderer: Union[Unset, None, str] = UNSET,
    is_receiver: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
) -> Response[List[ContactAddress]]:
    """
    Args:
        account (Union[Unset, None, str]):
        client (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ContactAddressesListFormat]):
        is_orderer (Union[Unset, None, str]):
        is_receiver (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        source (Union[Unset, None, str]):

    Returns:
        Response[List[ContactAddress]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        client=client,
        cursor=cursor,
        format_=format_,
        is_orderer=is_orderer,
        is_receiver=is_receiver,
        ordering=ordering,
        page_size=page_size,
        search=search,
        source=source,
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
    client: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ContactAddressesListFormat] = UNSET,
    is_orderer: Union[Unset, None, str] = UNSET,
    is_receiver: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
) -> Optional[List[ContactAddress]]:
    """
    Args:
        account (Union[Unset, None, str]):
        client (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ContactAddressesListFormat]):
        is_orderer (Union[Unset, None, str]):
        is_receiver (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        source (Union[Unset, None, str]):

    Returns:
        Response[List[ContactAddress]]
    """

    return sync_detailed(
        client=client,
        account=account,
        client=client,
        cursor=cursor,
        format_=format_,
        is_orderer=is_orderer,
        is_receiver=is_receiver,
        ordering=ordering,
        page_size=page_size,
        search=search,
        source=source,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    client: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ContactAddressesListFormat] = UNSET,
    is_orderer: Union[Unset, None, str] = UNSET,
    is_receiver: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
) -> Response[List[ContactAddress]]:
    """
    Args:
        account (Union[Unset, None, str]):
        client (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ContactAddressesListFormat]):
        is_orderer (Union[Unset, None, str]):
        is_receiver (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        source (Union[Unset, None, str]):

    Returns:
        Response[List[ContactAddress]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        client=client,
        cursor=cursor,
        format_=format_,
        is_orderer=is_orderer,
        is_receiver=is_receiver,
        ordering=ordering,
        page_size=page_size,
        search=search,
        source=source,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    client: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ContactAddressesListFormat] = UNSET,
    is_orderer: Union[Unset, None, str] = UNSET,
    is_receiver: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
) -> Optional[List[ContactAddress]]:
    """
    Args:
        account (Union[Unset, None, str]):
        client (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ContactAddressesListFormat]):
        is_orderer (Union[Unset, None, str]):
        is_receiver (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        source (Union[Unset, None, str]):

    Returns:
        Response[List[ContactAddress]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            client=client,
            cursor=cursor,
            format_=format_,
            is_orderer=is_orderer,
            is_receiver=is_receiver,
            ordering=ordering,
            page_size=page_size,
            search=search,
            source=source,
        )
    ).parsed

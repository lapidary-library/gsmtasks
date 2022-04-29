from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.contact_address_background_import import ContactAddressBackgroundImport
from ...models.contact_address_import_list_format import ContactAddressImportListFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ContactAddressImportListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/contact_address_import/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["cursor"] = cursor

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ContactAddressBackgroundImport]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_contact_address_background_import_list_item_data in _response_200:
            componentsschemas_paginated_contact_address_background_import_list_item = (
                ContactAddressBackgroundImport.from_dict(
                    componentsschemas_paginated_contact_address_background_import_list_item_data
                )
            )

            response_200.append(componentsschemas_paginated_contact_address_background_import_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ContactAddressBackgroundImport]]:
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
    format_: Union[Unset, None, ContactAddressImportListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[List[ContactAddressBackgroundImport]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ContactAddressImportListFormat]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[ContactAddressBackgroundImport]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
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
    format_: Union[Unset, None, ContactAddressImportListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[List[ContactAddressBackgroundImport]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ContactAddressImportListFormat]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[ContactAddressBackgroundImport]]
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ContactAddressImportListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[List[ContactAddressBackgroundImport]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ContactAddressImportListFormat]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[ContactAddressBackgroundImport]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, ContactAddressImportListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[List[ContactAddressBackgroundImport]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, ContactAddressImportListFormat]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[ContactAddressBackgroundImport]]
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            format_=format_,
            page_size=page_size,
        )
    ).parsed

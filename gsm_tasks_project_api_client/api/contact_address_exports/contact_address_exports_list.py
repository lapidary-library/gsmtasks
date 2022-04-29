from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.contact_address_export import ContactAddressExport
from ...models.contact_address_exports_list_format import ContactAddressExportsListFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, ContactAddressExportsListFormat] = ContactAddressExportsListFormat.JSON,
    is_orderer: Union[Unset, None, str] = UNSET,
    is_receiver: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/contact_address_exports/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["fields"] = fields

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["is_orderer"] = is_orderer

    params["is_receiver"] = is_receiver

    params["ordering"] = ordering

    params["page"] = page

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


def _parse_response(*, response: httpx.Response) -> Optional[List[ContactAddressExport]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_contact_address_export_list_item_data in _response_200:
            componentsschemas_paginated_contact_address_export_list_item = ContactAddressExport.from_dict(
                componentsschemas_paginated_contact_address_export_list_item_data
            )

            response_200.append(componentsschemas_paginated_contact_address_export_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ContactAddressExport]]:
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
    fields: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, ContactAddressExportsListFormat] = ContactAddressExportsListFormat.JSON,
    is_orderer: Union[Unset, None, str] = UNSET,
    is_receiver: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
) -> Response[List[ContactAddressExport]]:
    """This view has multiple renderer classes available: `json` and `xlsx`. In order to export the data as
    an excel file, just set query argument `format` to `xlsx`.When downloading `xlsx` format, use Accept
    header `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; version=...`

    The user can request what fields and in what order will be rendered using query argument `fields`.
    This is a comma separated list of field names used in the API.

    When exporting to **excel**, the column names may be changed based on pre-defined field names and
    width mapping.

    Available since version 2.2.1

    Args:
        account (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):
        format_ (Union[Unset, None, ContactAddressExportsListFormat]):  Default:
            ContactAddressExportsListFormat.JSON.
        is_orderer (Union[Unset, None, str]):
        is_receiver (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        source (Union[Unset, None, str]):

    Returns:
        Response[List[ContactAddressExport]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        fields=fields,
        format_=format_,
        is_orderer=is_orderer,
        is_receiver=is_receiver,
        ordering=ordering,
        page=page,
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
    fields: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, ContactAddressExportsListFormat] = ContactAddressExportsListFormat.JSON,
    is_orderer: Union[Unset, None, str] = UNSET,
    is_receiver: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
) -> Optional[List[ContactAddressExport]]:
    """This view has multiple renderer classes available: `json` and `xlsx`. In order to export the data as
    an excel file, just set query argument `format` to `xlsx`.When downloading `xlsx` format, use Accept
    header `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; version=...`

    The user can request what fields and in what order will be rendered using query argument `fields`.
    This is a comma separated list of field names used in the API.

    When exporting to **excel**, the column names may be changed based on pre-defined field names and
    width mapping.

    Available since version 2.2.1

    Args:
        account (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):
        format_ (Union[Unset, None, ContactAddressExportsListFormat]):  Default:
            ContactAddressExportsListFormat.JSON.
        is_orderer (Union[Unset, None, str]):
        is_receiver (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        source (Union[Unset, None, str]):

    Returns:
        Response[List[ContactAddressExport]]
    """

    return sync_detailed(
        client=client,
        account=account,
        fields=fields,
        format_=format_,
        is_orderer=is_orderer,
        is_receiver=is_receiver,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
        source=source,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, ContactAddressExportsListFormat] = ContactAddressExportsListFormat.JSON,
    is_orderer: Union[Unset, None, str] = UNSET,
    is_receiver: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
) -> Response[List[ContactAddressExport]]:
    """This view has multiple renderer classes available: `json` and `xlsx`. In order to export the data as
    an excel file, just set query argument `format` to `xlsx`.When downloading `xlsx` format, use Accept
    header `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; version=...`

    The user can request what fields and in what order will be rendered using query argument `fields`.
    This is a comma separated list of field names used in the API.

    When exporting to **excel**, the column names may be changed based on pre-defined field names and
    width mapping.

    Available since version 2.2.1

    Args:
        account (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):
        format_ (Union[Unset, None, ContactAddressExportsListFormat]):  Default:
            ContactAddressExportsListFormat.JSON.
        is_orderer (Union[Unset, None, str]):
        is_receiver (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        source (Union[Unset, None, str]):

    Returns:
        Response[List[ContactAddressExport]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        fields=fields,
        format_=format_,
        is_orderer=is_orderer,
        is_receiver=is_receiver,
        ordering=ordering,
        page=page,
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
    fields: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, ContactAddressExportsListFormat] = ContactAddressExportsListFormat.JSON,
    is_orderer: Union[Unset, None, str] = UNSET,
    is_receiver: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
) -> Optional[List[ContactAddressExport]]:
    """This view has multiple renderer classes available: `json` and `xlsx`. In order to export the data as
    an excel file, just set query argument `format` to `xlsx`.When downloading `xlsx` format, use Accept
    header `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; version=...`

    The user can request what fields and in what order will be rendered using query argument `fields`.
    This is a comma separated list of field names used in the API.

    When exporting to **excel**, the column names may be changed based on pre-defined field names and
    width mapping.

    Available since version 2.2.1

    Args:
        account (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):
        format_ (Union[Unset, None, ContactAddressExportsListFormat]):  Default:
            ContactAddressExportsListFormat.JSON.
        is_orderer (Union[Unset, None, str]):
        is_receiver (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        source (Union[Unset, None, str]):

    Returns:
        Response[List[ContactAddressExport]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            fields=fields,
            format_=format_,
            is_orderer=is_orderer,
            is_receiver=is_receiver,
            ordering=ordering,
            page=page,
            page_size=page_size,
            search=search,
            source=source,
        )
    ).parsed

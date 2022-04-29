from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.billing_invoices_list_billing_method import BillingInvoicesListBillingMethod
from ...models.billing_invoices_list_format import BillingInvoicesListFormat
from ...models.billing_invoices_list_state import BillingInvoicesListState
from ...models.invoice import Invoice
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    billing_method: Union[Unset, None, BillingInvoicesListBillingMethod] = UNSET,
    created_at: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, BillingInvoicesListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingInvoicesListState] = UNSET,
) -> Dict[str, Any]:
    url = "{}/billing/invoices/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    json_billing_method: Union[Unset, None, str] = UNSET
    if not isinstance(billing_method, Unset):
        json_billing_method = billing_method.value if billing_method else None

    params["billing_method"] = json_billing_method

    params["created_at"] = created_at

    params["cursor"] = cursor

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["page_size"] = page_size

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Invoice]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_invoice_list_item_data in _response_200:
            componentsschemas_paginated_invoice_list_item = Invoice.from_dict(
                componentsschemas_paginated_invoice_list_item_data
            )

            response_200.append(componentsschemas_paginated_invoice_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Invoice]]:
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
    billing_method: Union[Unset, None, BillingInvoicesListBillingMethod] = UNSET,
    created_at: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, BillingInvoicesListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingInvoicesListState] = UNSET,
) -> Response[List[Invoice]]:
    """
    Args:
        account (Union[Unset, None, str]):
        billing_method (Union[Unset, None, BillingInvoicesListBillingMethod]):
        created_at (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, BillingInvoicesListFormat]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, BillingInvoicesListState]):

    Returns:
        Response[List[Invoice]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        billing_method=billing_method,
        created_at=created_at,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
        state=state,
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
    billing_method: Union[Unset, None, BillingInvoicesListBillingMethod] = UNSET,
    created_at: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, BillingInvoicesListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingInvoicesListState] = UNSET,
) -> Optional[List[Invoice]]:
    """
    Args:
        account (Union[Unset, None, str]):
        billing_method (Union[Unset, None, BillingInvoicesListBillingMethod]):
        created_at (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, BillingInvoicesListFormat]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, BillingInvoicesListState]):

    Returns:
        Response[List[Invoice]]
    """

    return sync_detailed(
        client=client,
        account=account,
        billing_method=billing_method,
        created_at=created_at,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    billing_method: Union[Unset, None, BillingInvoicesListBillingMethod] = UNSET,
    created_at: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, BillingInvoicesListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingInvoicesListState] = UNSET,
) -> Response[List[Invoice]]:
    """
    Args:
        account (Union[Unset, None, str]):
        billing_method (Union[Unset, None, BillingInvoicesListBillingMethod]):
        created_at (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, BillingInvoicesListFormat]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, BillingInvoicesListState]):

    Returns:
        Response[List[Invoice]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        billing_method=billing_method,
        created_at=created_at,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
        state=state,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    billing_method: Union[Unset, None, BillingInvoicesListBillingMethod] = UNSET,
    created_at: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, BillingInvoicesListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingInvoicesListState] = UNSET,
) -> Optional[List[Invoice]]:
    """
    Args:
        account (Union[Unset, None, str]):
        billing_method (Union[Unset, None, BillingInvoicesListBillingMethod]):
        created_at (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, BillingInvoicesListFormat]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, BillingInvoicesListState]):

    Returns:
        Response[List[Invoice]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            billing_method=billing_method,
            created_at=created_at,
            cursor=cursor,
            format_=format_,
            page_size=page_size,
            state=state,
        )
    ).parsed

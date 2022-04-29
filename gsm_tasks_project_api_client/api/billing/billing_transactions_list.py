from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.billing_transactions_list_format import BillingTransactionsListFormat
from ...models.billing_transactions_list_state import BillingTransactionsListState
from ...models.braintree_transaction import BraintreeTransaction
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    customer: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, BillingTransactionsListFormat] = UNSET,
    invoice_account: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingTransactionsListState] = UNSET,
) -> Dict[str, Any]:
    url = "{}/billing/transactions/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["cursor"] = cursor

    params["customer"] = customer

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["invoice__account"] = invoice_account

    params["ordering"] = ordering

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


def _parse_response(*, response: httpx.Response) -> Optional[List[BraintreeTransaction]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_braintree_transaction_list_item_data in _response_200:
            componentsschemas_paginated_braintree_transaction_list_item = BraintreeTransaction.from_dict(
                componentsschemas_paginated_braintree_transaction_list_item_data
            )

            response_200.append(componentsschemas_paginated_braintree_transaction_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[BraintreeTransaction]]:
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
    customer: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, BillingTransactionsListFormat] = UNSET,
    invoice_account: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingTransactionsListState] = UNSET,
) -> Response[List[BraintreeTransaction]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        customer (Union[Unset, None, str]):
        format_ (Union[Unset, None, BillingTransactionsListFormat]):
        invoice_account (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, BillingTransactionsListState]):

    Returns:
        Response[List[BraintreeTransaction]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        customer=customer,
        format_=format_,
        invoice_account=invoice_account,
        ordering=ordering,
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
    cursor: Union[Unset, None, int] = UNSET,
    customer: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, BillingTransactionsListFormat] = UNSET,
    invoice_account: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingTransactionsListState] = UNSET,
) -> Optional[List[BraintreeTransaction]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        customer (Union[Unset, None, str]):
        format_ (Union[Unset, None, BillingTransactionsListFormat]):
        invoice_account (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, BillingTransactionsListState]):

    Returns:
        Response[List[BraintreeTransaction]]
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        customer=customer,
        format_=format_,
        invoice_account=invoice_account,
        ordering=ordering,
        page_size=page_size,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    customer: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, BillingTransactionsListFormat] = UNSET,
    invoice_account: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingTransactionsListState] = UNSET,
) -> Response[List[BraintreeTransaction]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        customer (Union[Unset, None, str]):
        format_ (Union[Unset, None, BillingTransactionsListFormat]):
        invoice_account (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, BillingTransactionsListState]):

    Returns:
        Response[List[BraintreeTransaction]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        customer=customer,
        format_=format_,
        invoice_account=invoice_account,
        ordering=ordering,
        page_size=page_size,
        state=state,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    customer: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, BillingTransactionsListFormat] = UNSET,
    invoice_account: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingTransactionsListState] = UNSET,
) -> Optional[List[BraintreeTransaction]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        customer (Union[Unset, None, str]):
        format_ (Union[Unset, None, BillingTransactionsListFormat]):
        invoice_account (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, BillingTransactionsListState]):

    Returns:
        Response[List[BraintreeTransaction]]
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            customer=customer,
            format_=format_,
            invoice_account=invoice_account,
            ordering=ordering,
            page_size=page_size,
            state=state,
        )
    ).parsed

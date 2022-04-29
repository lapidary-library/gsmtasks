from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.billing_stripe_payments_list_format import BillingStripePaymentsListFormat
from ...models.billing_stripe_payments_list_state import BillingStripePaymentsListState
from ...models.billing_stripe_payments_list_stripe_state import BillingStripePaymentsListStripeState
from ...models.stripe_payment import StripePayment
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    billable_account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, BillingStripePaymentsListFormat] = UNSET,
    invoice: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingStripePaymentsListState] = UNSET,
    stripe_state: Union[Unset, None, BillingStripePaymentsListStripeState] = UNSET,
) -> Dict[str, Any]:
    url = "{}/billing/stripe_payments/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["billable_account"] = billable_account

    params["cursor"] = cursor

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["invoice"] = invoice

    params["ordering"] = ordering

    params["page_size"] = page_size

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    json_stripe_state: Union[Unset, None, str] = UNSET
    if not isinstance(stripe_state, Unset):
        json_stripe_state = stripe_state.value if stripe_state else None

    params["stripe_state"] = json_stripe_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[StripePayment]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_stripe_payment_list_item_data in _response_200:
            componentsschemas_paginated_stripe_payment_list_item = StripePayment.from_dict(
                componentsschemas_paginated_stripe_payment_list_item_data
            )

            response_200.append(componentsschemas_paginated_stripe_payment_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[StripePayment]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    billable_account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, BillingStripePaymentsListFormat] = UNSET,
    invoice: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingStripePaymentsListState] = UNSET,
    stripe_state: Union[Unset, None, BillingStripePaymentsListStripeState] = UNSET,
) -> Response[List[StripePayment]]:
    """
    Args:
        billable_account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, BillingStripePaymentsListFormat]):
        invoice (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, BillingStripePaymentsListState]):
        stripe_state (Union[Unset, None, BillingStripePaymentsListStripeState]):

    Returns:
        Response[List[StripePayment]]
    """

    kwargs = _get_kwargs(
        client=client,
        billable_account=billable_account,
        cursor=cursor,
        format_=format_,
        invoice=invoice,
        ordering=ordering,
        page_size=page_size,
        state=state,
        stripe_state=stripe_state,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    billable_account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, BillingStripePaymentsListFormat] = UNSET,
    invoice: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingStripePaymentsListState] = UNSET,
    stripe_state: Union[Unset, None, BillingStripePaymentsListStripeState] = UNSET,
) -> Optional[List[StripePayment]]:
    """
    Args:
        billable_account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, BillingStripePaymentsListFormat]):
        invoice (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, BillingStripePaymentsListState]):
        stripe_state (Union[Unset, None, BillingStripePaymentsListStripeState]):

    Returns:
        Response[List[StripePayment]]
    """

    return sync_detailed(
        client=client,
        billable_account=billable_account,
        cursor=cursor,
        format_=format_,
        invoice=invoice,
        ordering=ordering,
        page_size=page_size,
        state=state,
        stripe_state=stripe_state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    billable_account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, BillingStripePaymentsListFormat] = UNSET,
    invoice: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingStripePaymentsListState] = UNSET,
    stripe_state: Union[Unset, None, BillingStripePaymentsListStripeState] = UNSET,
) -> Response[List[StripePayment]]:
    """
    Args:
        billable_account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, BillingStripePaymentsListFormat]):
        invoice (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, BillingStripePaymentsListState]):
        stripe_state (Union[Unset, None, BillingStripePaymentsListStripeState]):

    Returns:
        Response[List[StripePayment]]
    """

    kwargs = _get_kwargs(
        client=client,
        billable_account=billable_account,
        cursor=cursor,
        format_=format_,
        invoice=invoice,
        ordering=ordering,
        page_size=page_size,
        state=state,
        stripe_state=stripe_state,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    billable_account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, BillingStripePaymentsListFormat] = UNSET,
    invoice: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, BillingStripePaymentsListState] = UNSET,
    stripe_state: Union[Unset, None, BillingStripePaymentsListStripeState] = UNSET,
) -> Optional[List[StripePayment]]:
    """
    Args:
        billable_account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, BillingStripePaymentsListFormat]):
        invoice (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, BillingStripePaymentsListState]):
        stripe_state (Union[Unset, None, BillingStripePaymentsListStripeState]):

    Returns:
        Response[List[StripePayment]]
    """

    return (
        await asyncio_detailed(
            client=client,
            billable_account=billable_account,
            cursor=cursor,
            format_=format_,
            invoice=invoice,
            ordering=ordering,
            page_size=page_size,
            state=state,
            stripe_state=stripe_state,
        )
    ).parsed

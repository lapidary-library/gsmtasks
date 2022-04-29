from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.billing_transactions_retrieve_format import BillingTransactionsRetrieveFormat
from ...models.braintree_transaction import BraintreeTransaction
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, BillingTransactionsRetrieveFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/billing/transactions/{id}/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[BraintreeTransaction]:
    if response.status_code == 200:
        response_200 = BraintreeTransaction.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[BraintreeTransaction]:
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
    format_: Union[Unset, None, BillingTransactionsRetrieveFormat] = UNSET,
) -> Response[BraintreeTransaction]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, BillingTransactionsRetrieveFormat]):

    Returns:
        Response[BraintreeTransaction]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        format_=format_,
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
    format_: Union[Unset, None, BillingTransactionsRetrieveFormat] = UNSET,
) -> Optional[BraintreeTransaction]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, BillingTransactionsRetrieveFormat]):

    Returns:
        Response[BraintreeTransaction]
    """

    return sync_detailed(
        id=id,
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, BillingTransactionsRetrieveFormat] = UNSET,
) -> Response[BraintreeTransaction]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, BillingTransactionsRetrieveFormat]):

    Returns:
        Response[BraintreeTransaction]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, BillingTransactionsRetrieveFormat] = UNSET,
) -> Optional[BraintreeTransaction]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, BillingTransactionsRetrieveFormat]):

    Returns:
        Response[BraintreeTransaction]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            format_=format_,
        )
    ).parsed

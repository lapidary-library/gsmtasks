from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.account_stripe_payment_methods import AccountStripePaymentMethods
from ...models.accounts_stripe_payment_methods_retrieve_format import AccountsStripePaymentMethodsRetrieveFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, AccountsStripePaymentMethodsRetrieveFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/accounts/{id}/stripe_payment_methods/".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[AccountStripePaymentMethods]:
    if response.status_code == 200:
        response_200 = AccountStripePaymentMethods.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AccountStripePaymentMethods]:
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
    format_: Union[Unset, None, AccountsStripePaymentMethodsRetrieveFormat] = UNSET,
) -> Response[AccountStripePaymentMethods]:
    """Fetch all customer payment methods.
    This includes all attached payment methods, default method_id

    Args:
        id (str):
        format_ (Union[Unset, None, AccountsStripePaymentMethodsRetrieveFormat]):

    Returns:
        Response[AccountStripePaymentMethods]
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
    format_: Union[Unset, None, AccountsStripePaymentMethodsRetrieveFormat] = UNSET,
) -> Optional[AccountStripePaymentMethods]:
    """Fetch all customer payment methods.
    This includes all attached payment methods, default method_id

    Args:
        id (str):
        format_ (Union[Unset, None, AccountsStripePaymentMethodsRetrieveFormat]):

    Returns:
        Response[AccountStripePaymentMethods]
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
    format_: Union[Unset, None, AccountsStripePaymentMethodsRetrieveFormat] = UNSET,
) -> Response[AccountStripePaymentMethods]:
    """Fetch all customer payment methods.
    This includes all attached payment methods, default method_id

    Args:
        id (str):
        format_ (Union[Unset, None, AccountsStripePaymentMethodsRetrieveFormat]):

    Returns:
        Response[AccountStripePaymentMethods]
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
    format_: Union[Unset, None, AccountsStripePaymentMethodsRetrieveFormat] = UNSET,
) -> Optional[AccountStripePaymentMethods]:
    """Fetch all customer payment methods.
    This includes all attached payment methods, default method_id

    Args:
        id (str):
        format_ (Union[Unset, None, AccountsStripePaymentMethodsRetrieveFormat]):

    Returns:
        Response[AccountStripePaymentMethods]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            format_=format_,
        )
    ).parsed

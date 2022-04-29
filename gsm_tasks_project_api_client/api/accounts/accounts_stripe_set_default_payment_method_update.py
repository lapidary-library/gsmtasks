from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.account_stripe_payment_method_set_default import AccountStripePaymentMethodSetDefault
from ...models.accounts_stripe_set_default_payment_method_update_format import (
    AccountsStripeSetDefaultPaymentMethodUpdateFormat,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: AccountStripePaymentMethodSetDefault,
    multipart_data: AccountStripePaymentMethodSetDefault,
    json_body: AccountStripePaymentMethodSetDefault,
    format_: Union[Unset, None, AccountsStripeSetDefaultPaymentMethodUpdateFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/accounts/{id}/stripe_set_default_payment_method/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AccountStripePaymentMethodSetDefault]:
    if response.status_code == 200:
        response_200 = AccountStripePaymentMethodSetDefault.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AccountStripePaymentMethodSetDefault]:
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
    form_data: AccountStripePaymentMethodSetDefault,
    multipart_data: AccountStripePaymentMethodSetDefault,
    json_body: AccountStripePaymentMethodSetDefault,
    format_: Union[Unset, None, AccountsStripeSetDefaultPaymentMethodUpdateFormat] = UNSET,
) -> Response[AccountStripePaymentMethodSetDefault]:
    """Action to set a payment method to default.

    Args:
        id (str):
        format_ (Union[Unset, None, AccountsStripeSetDefaultPaymentMethodUpdateFormat]):
        multipart_data (AccountStripePaymentMethodSetDefault):
        json_body (AccountStripePaymentMethodSetDefault):

    Returns:
        Response[AccountStripePaymentMethodSetDefault]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
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
    form_data: AccountStripePaymentMethodSetDefault,
    multipart_data: AccountStripePaymentMethodSetDefault,
    json_body: AccountStripePaymentMethodSetDefault,
    format_: Union[Unset, None, AccountsStripeSetDefaultPaymentMethodUpdateFormat] = UNSET,
) -> Optional[AccountStripePaymentMethodSetDefault]:
    """Action to set a payment method to default.

    Args:
        id (str):
        format_ (Union[Unset, None, AccountsStripeSetDefaultPaymentMethodUpdateFormat]):
        multipart_data (AccountStripePaymentMethodSetDefault):
        json_body (AccountStripePaymentMethodSetDefault):

    Returns:
        Response[AccountStripePaymentMethodSetDefault]
    """

    return sync_detailed(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: AccountStripePaymentMethodSetDefault,
    multipart_data: AccountStripePaymentMethodSetDefault,
    json_body: AccountStripePaymentMethodSetDefault,
    format_: Union[Unset, None, AccountsStripeSetDefaultPaymentMethodUpdateFormat] = UNSET,
) -> Response[AccountStripePaymentMethodSetDefault]:
    """Action to set a payment method to default.

    Args:
        id (str):
        format_ (Union[Unset, None, AccountsStripeSetDefaultPaymentMethodUpdateFormat]):
        multipart_data (AccountStripePaymentMethodSetDefault):
        json_body (AccountStripePaymentMethodSetDefault):

    Returns:
        Response[AccountStripePaymentMethodSetDefault]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: AccountStripePaymentMethodSetDefault,
    multipart_data: AccountStripePaymentMethodSetDefault,
    json_body: AccountStripePaymentMethodSetDefault,
    format_: Union[Unset, None, AccountsStripeSetDefaultPaymentMethodUpdateFormat] = UNSET,
) -> Optional[AccountStripePaymentMethodSetDefault]:
    """Action to set a payment method to default.

    Args:
        id (str):
        format_ (Union[Unset, None, AccountsStripeSetDefaultPaymentMethodUpdateFormat]):
        multipart_data (AccountStripePaymentMethodSetDefault):
        json_body (AccountStripePaymentMethodSetDefault):

    Returns:
        Response[AccountStripePaymentMethodSetDefault]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
            format_=format_,
        )
    ).parsed

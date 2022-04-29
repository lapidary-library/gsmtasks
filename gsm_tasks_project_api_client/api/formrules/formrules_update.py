from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.form_rule import FormRule
from ...models.formrules_update_format import FormrulesUpdateFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: FormRule,
    multipart_data: FormRule,
    json_body: FormRule,
    format_: Union[Unset, None, FormrulesUpdateFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/formrules/{id}/".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[FormRule]:
    if response.status_code == 200:
        response_200 = FormRule.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[FormRule]:
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
    form_data: FormRule,
    multipart_data: FormRule,
    json_body: FormRule,
    format_: Union[Unset, None, FormrulesUpdateFormat] = UNSET,
) -> Response[FormRule]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, FormrulesUpdateFormat]):
        multipart_data (FormRule):
        json_body (FormRule):

    Returns:
        Response[FormRule]
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
    form_data: FormRule,
    multipart_data: FormRule,
    json_body: FormRule,
    format_: Union[Unset, None, FormrulesUpdateFormat] = UNSET,
) -> Optional[FormRule]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, FormrulesUpdateFormat]):
        multipart_data (FormRule):
        json_body (FormRule):

    Returns:
        Response[FormRule]
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
    form_data: FormRule,
    multipart_data: FormRule,
    json_body: FormRule,
    format_: Union[Unset, None, FormrulesUpdateFormat] = UNSET,
) -> Response[FormRule]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, FormrulesUpdateFormat]):
        multipart_data (FormRule):
        json_body (FormRule):

    Returns:
        Response[FormRule]
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
    form_data: FormRule,
    multipart_data: FormRule,
    json_body: FormRule,
    format_: Union[Unset, None, FormrulesUpdateFormat] = UNSET,
) -> Optional[FormRule]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, FormrulesUpdateFormat]):
        multipart_data (FormRule):
        json_body (FormRule):

    Returns:
        Response[FormRule]
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

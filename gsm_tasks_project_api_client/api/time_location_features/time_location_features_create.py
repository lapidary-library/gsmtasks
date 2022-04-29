from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.time_location_feature import TimeLocationFeature
from ...models.time_location_features_create_format import TimeLocationFeaturesCreateFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: TimeLocationFeature,
    multipart_data: TimeLocationFeature,
    json_body: TimeLocationFeature,
    format_: Union[Unset, None, TimeLocationFeaturesCreateFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/time_location_features/".format(client.base_url)

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
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[TimeLocationFeature]:
    if response.status_code == 201:
        response_201 = TimeLocationFeature.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[TimeLocationFeature]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: TimeLocationFeature,
    multipart_data: TimeLocationFeature,
    json_body: TimeLocationFeature,
    format_: Union[Unset, None, TimeLocationFeaturesCreateFormat] = UNSET,
) -> Response[TimeLocationFeature]:
    """
    Args:
        format_ (Union[Unset, None, TimeLocationFeaturesCreateFormat]):
        multipart_data (TimeLocationFeature): A subclass of ModelSerializer
            that outputs geojson-ready data as
            features and feature collections
        json_body (TimeLocationFeature): A subclass of ModelSerializer
            that outputs geojson-ready data as
            features and feature collections

    Returns:
        Response[TimeLocationFeature]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    form_data: TimeLocationFeature,
    multipart_data: TimeLocationFeature,
    json_body: TimeLocationFeature,
    format_: Union[Unset, None, TimeLocationFeaturesCreateFormat] = UNSET,
) -> Optional[TimeLocationFeature]:
    """
    Args:
        format_ (Union[Unset, None, TimeLocationFeaturesCreateFormat]):
        multipart_data (TimeLocationFeature): A subclass of ModelSerializer
            that outputs geojson-ready data as
            features and feature collections
        json_body (TimeLocationFeature): A subclass of ModelSerializer
            that outputs geojson-ready data as
            features and feature collections

    Returns:
        Response[TimeLocationFeature]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: TimeLocationFeature,
    multipart_data: TimeLocationFeature,
    json_body: TimeLocationFeature,
    format_: Union[Unset, None, TimeLocationFeaturesCreateFormat] = UNSET,
) -> Response[TimeLocationFeature]:
    """
    Args:
        format_ (Union[Unset, None, TimeLocationFeaturesCreateFormat]):
        multipart_data (TimeLocationFeature): A subclass of ModelSerializer
            that outputs geojson-ready data as
            features and feature collections
        json_body (TimeLocationFeature): A subclass of ModelSerializer
            that outputs geojson-ready data as
            features and feature collections

    Returns:
        Response[TimeLocationFeature]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    form_data: TimeLocationFeature,
    multipart_data: TimeLocationFeature,
    json_body: TimeLocationFeature,
    format_: Union[Unset, None, TimeLocationFeaturesCreateFormat] = UNSET,
) -> Optional[TimeLocationFeature]:
    """
    Args:
        format_ (Union[Unset, None, TimeLocationFeaturesCreateFormat]):
        multipart_data (TimeLocationFeature): A subclass of ModelSerializer
            that outputs geojson-ready data as
            features and feature collections
        json_body (TimeLocationFeature): A subclass of ModelSerializer
            that outputs geojson-ready data as
            features and feature collections

    Returns:
        Response[TimeLocationFeature]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
            format_=format_,
        )
    ).parsed

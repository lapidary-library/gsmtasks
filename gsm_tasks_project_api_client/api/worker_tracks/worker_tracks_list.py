from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.worker_track import WorkerTrack
from ...models.worker_tracks_list_format import WorkerTracksListFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, WorkerTracksListFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/worker_tracks/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[List[WorkerTrack]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = WorkerTrack.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[WorkerTrack]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, WorkerTracksListFormat] = UNSET,
) -> Response[List[WorkerTrack]]:
    """
    Args:
        format_ (Union[Unset, None, WorkerTracksListFormat]):

    Returns:
        Response[List[WorkerTrack]]
    """

    kwargs = _get_kwargs(
        client=client,
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
    format_: Union[Unset, None, WorkerTracksListFormat] = UNSET,
) -> Optional[List[WorkerTrack]]:
    """
    Args:
        format_ (Union[Unset, None, WorkerTracksListFormat]):

    Returns:
        Response[List[WorkerTrack]]
    """

    return sync_detailed(
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, WorkerTracksListFormat] = UNSET,
) -> Response[List[WorkerTrack]]:
    """
    Args:
        format_ (Union[Unset, None, WorkerTracksListFormat]):

    Returns:
        Response[List[WorkerTrack]]
    """

    kwargs = _get_kwargs(
        client=client,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, WorkerTracksListFormat] = UNSET,
) -> Optional[List[WorkerTrack]]:
    """
    Args:
        format_ (Union[Unset, None, WorkerTracksListFormat]):

    Returns:
        Response[List[WorkerTrack]]
    """

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
        )
    ).parsed

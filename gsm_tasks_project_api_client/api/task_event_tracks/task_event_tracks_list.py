from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.task_event_track import TaskEventTrack
from ...models.task_event_tracks_list_event import TaskEventTracksListEvent
from ...models.task_event_tracks_list_format import TaskEventTracksListFormat
from ...models.task_event_tracks_list_from_state import TaskEventTracksListFromState
from ...models.task_event_tracks_list_to_state import TaskEventTracksListToState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, TaskEventTracksListEvent] = UNSET,
    format_: Union[Unset, None, TaskEventTracksListFormat] = UNSET,
    from_state: Union[Unset, None, TaskEventTracksListFromState] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    to_state: Union[Unset, None, TaskEventTracksListToState] = UNSET,
) -> Dict[str, Any]:
    url = "{}/task_event_tracks/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["cursor"] = cursor

    json_event: Union[Unset, None, str] = UNSET
    if not isinstance(event, Unset):
        json_event = event.value if event else None

    params["event"] = json_event

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    json_from_state: Union[Unset, None, str] = UNSET
    if not isinstance(from_state, Unset):
        json_from_state = from_state.value if from_state else None

    params["from_state"] = json_from_state

    params["ordering"] = ordering

    params["page_size"] = page_size

    json_to_state: Union[Unset, None, str] = UNSET
    if not isinstance(to_state, Unset):
        json_to_state = to_state.value if to_state else None

    params["to_state"] = json_to_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[TaskEventTrack]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_task_event_track_list_item_data in _response_200:
            componentsschemas_paginated_task_event_track_list_item = TaskEventTrack.from_dict(
                componentsschemas_paginated_task_event_track_list_item_data
            )

            response_200.append(componentsschemas_paginated_task_event_track_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[TaskEventTrack]]:
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
    event: Union[Unset, None, TaskEventTracksListEvent] = UNSET,
    format_: Union[Unset, None, TaskEventTracksListFormat] = UNSET,
    from_state: Union[Unset, None, TaskEventTracksListFromState] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    to_state: Union[Unset, None, TaskEventTracksListToState] = UNSET,
) -> Response[List[TaskEventTrack]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, TaskEventTracksListEvent]):
        format_ (Union[Unset, None, TaskEventTracksListFormat]):
        from_state (Union[Unset, None, TaskEventTracksListFromState]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        to_state (Union[Unset, None, TaskEventTracksListToState]):

    Returns:
        Response[List[TaskEventTrack]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        event=event,
        format_=format_,
        from_state=from_state,
        ordering=ordering,
        page_size=page_size,
        to_state=to_state,
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
    event: Union[Unset, None, TaskEventTracksListEvent] = UNSET,
    format_: Union[Unset, None, TaskEventTracksListFormat] = UNSET,
    from_state: Union[Unset, None, TaskEventTracksListFromState] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    to_state: Union[Unset, None, TaskEventTracksListToState] = UNSET,
) -> Optional[List[TaskEventTrack]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, TaskEventTracksListEvent]):
        format_ (Union[Unset, None, TaskEventTracksListFormat]):
        from_state (Union[Unset, None, TaskEventTracksListFromState]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        to_state (Union[Unset, None, TaskEventTracksListToState]):

    Returns:
        Response[List[TaskEventTrack]]
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        event=event,
        format_=format_,
        from_state=from_state,
        ordering=ordering,
        page_size=page_size,
        to_state=to_state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, TaskEventTracksListEvent] = UNSET,
    format_: Union[Unset, None, TaskEventTracksListFormat] = UNSET,
    from_state: Union[Unset, None, TaskEventTracksListFromState] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    to_state: Union[Unset, None, TaskEventTracksListToState] = UNSET,
) -> Response[List[TaskEventTrack]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, TaskEventTracksListEvent]):
        format_ (Union[Unset, None, TaskEventTracksListFormat]):
        from_state (Union[Unset, None, TaskEventTracksListFromState]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        to_state (Union[Unset, None, TaskEventTracksListToState]):

    Returns:
        Response[List[TaskEventTrack]]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
        event=event,
        format_=format_,
        from_state=from_state,
        ordering=ordering,
        page_size=page_size,
        to_state=to_state,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, TaskEventTracksListEvent] = UNSET,
    format_: Union[Unset, None, TaskEventTracksListFormat] = UNSET,
    from_state: Union[Unset, None, TaskEventTracksListFromState] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    to_state: Union[Unset, None, TaskEventTracksListToState] = UNSET,
) -> Optional[List[TaskEventTrack]]:
    """
    Args:
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, TaskEventTracksListEvent]):
        format_ (Union[Unset, None, TaskEventTracksListFormat]):
        from_state (Union[Unset, None, TaskEventTracksListFromState]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        to_state (Union[Unset, None, TaskEventTracksListToState]):

    Returns:
        Response[List[TaskEventTrack]]
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            event=event,
            format_=format_,
            from_state=from_state,
            ordering=ordering,
            page_size=page_size,
            to_state=to_state,
        )
    ).parsed

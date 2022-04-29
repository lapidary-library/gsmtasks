from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.task_event_serializer_v2 import TaskEventSerializerV2
from ...models.task_events_list_event import TaskEventsListEvent
from ...models.task_events_list_field import TaskEventsListField
from ...models.task_events_list_format import TaskEventsListFormat
from ...models.task_events_list_from_state import TaskEventsListFromState
from ...models.task_events_list_to_state import TaskEventsListToState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, TaskEventsListEvent] = UNSET,
    event_in: Union[Unset, None, str] = UNSET,
    field: Union[Unset, None, TaskEventsListField] = UNSET,
    format_: Union[Unset, None, TaskEventsListFormat] = UNSET,
    from_state: Union[Unset, None, TaskEventsListFromState] = UNSET,
    from_state_in: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    task_account: Union[Unset, None, str] = UNSET,
    to_state: Union[Unset, None, TaskEventsListToState] = UNSET,
    to_state_in: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/task_events/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["assignee"] = assignee

    params["cursor"] = cursor

    json_event: Union[Unset, None, str] = UNSET
    if not isinstance(event, Unset):
        json_event = event.value if event else None

    params["event"] = json_event

    params["event__in"] = event_in

    json_field: Union[Unset, None, str] = UNSET
    if not isinstance(field, Unset):
        json_field = field.value if field else None

    params["field"] = json_field

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    json_from_state: Union[Unset, None, str] = UNSET
    if not isinstance(from_state, Unset):
        json_from_state = from_state.value if from_state else None

    params["from_state"] = json_from_state

    params["from_state__in"] = from_state_in

    params["ordering"] = ordering

    params["page_size"] = page_size

    params["task"] = task

    params["task__account"] = task_account

    json_to_state: Union[Unset, None, str] = UNSET
    if not isinstance(to_state, Unset):
        json_to_state = to_state.value if to_state else None

    params["to_state"] = json_to_state

    params["to_state__in"] = to_state_in

    params["user"] = user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[TaskEventSerializerV2]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_task_event_serializer_v2_list_item_data in _response_200:
            componentsschemas_paginated_task_event_serializer_v2_list_item = TaskEventSerializerV2.from_dict(
                componentsschemas_paginated_task_event_serializer_v2_list_item_data
            )

            response_200.append(componentsschemas_paginated_task_event_serializer_v2_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[TaskEventSerializerV2]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, TaskEventsListEvent] = UNSET,
    event_in: Union[Unset, None, str] = UNSET,
    field: Union[Unset, None, TaskEventsListField] = UNSET,
    format_: Union[Unset, None, TaskEventsListFormat] = UNSET,
    from_state: Union[Unset, None, TaskEventsListFromState] = UNSET,
    from_state_in: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    task_account: Union[Unset, None, str] = UNSET,
    to_state: Union[Unset, None, TaskEventsListToState] = UNSET,
    to_state_in: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Response[List[TaskEventSerializerV2]]:
    """Mixin which allows the override of the filename being
    passed back to the user when the spreadsheet is downloaded.

    Args:
        assignee (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, TaskEventsListEvent]):
        event_in (Union[Unset, None, str]):
        field (Union[Unset, None, TaskEventsListField]):
        format_ (Union[Unset, None, TaskEventsListFormat]):
        from_state (Union[Unset, None, TaskEventsListFromState]):
        from_state_in (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        task (Union[Unset, None, str]):
        task_account (Union[Unset, None, str]):
        to_state (Union[Unset, None, TaskEventsListToState]):
        to_state_in (Union[Unset, None, str]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[TaskEventSerializerV2]]
    """

    kwargs = _get_kwargs(
        client=client,
        assignee=assignee,
        cursor=cursor,
        event=event,
        event_in=event_in,
        field=field,
        format_=format_,
        from_state=from_state,
        from_state_in=from_state_in,
        ordering=ordering,
        page_size=page_size,
        task=task,
        task_account=task_account,
        to_state=to_state,
        to_state_in=to_state_in,
        user=user,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, TaskEventsListEvent] = UNSET,
    event_in: Union[Unset, None, str] = UNSET,
    field: Union[Unset, None, TaskEventsListField] = UNSET,
    format_: Union[Unset, None, TaskEventsListFormat] = UNSET,
    from_state: Union[Unset, None, TaskEventsListFromState] = UNSET,
    from_state_in: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    task_account: Union[Unset, None, str] = UNSET,
    to_state: Union[Unset, None, TaskEventsListToState] = UNSET,
    to_state_in: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Optional[List[TaskEventSerializerV2]]:
    """Mixin which allows the override of the filename being
    passed back to the user when the spreadsheet is downloaded.

    Args:
        assignee (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, TaskEventsListEvent]):
        event_in (Union[Unset, None, str]):
        field (Union[Unset, None, TaskEventsListField]):
        format_ (Union[Unset, None, TaskEventsListFormat]):
        from_state (Union[Unset, None, TaskEventsListFromState]):
        from_state_in (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        task (Union[Unset, None, str]):
        task_account (Union[Unset, None, str]):
        to_state (Union[Unset, None, TaskEventsListToState]):
        to_state_in (Union[Unset, None, str]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[TaskEventSerializerV2]]
    """

    return sync_detailed(
        client=client,
        assignee=assignee,
        cursor=cursor,
        event=event,
        event_in=event_in,
        field=field,
        format_=format_,
        from_state=from_state,
        from_state_in=from_state_in,
        ordering=ordering,
        page_size=page_size,
        task=task,
        task_account=task_account,
        to_state=to_state,
        to_state_in=to_state_in,
        user=user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, TaskEventsListEvent] = UNSET,
    event_in: Union[Unset, None, str] = UNSET,
    field: Union[Unset, None, TaskEventsListField] = UNSET,
    format_: Union[Unset, None, TaskEventsListFormat] = UNSET,
    from_state: Union[Unset, None, TaskEventsListFromState] = UNSET,
    from_state_in: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    task_account: Union[Unset, None, str] = UNSET,
    to_state: Union[Unset, None, TaskEventsListToState] = UNSET,
    to_state_in: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Response[List[TaskEventSerializerV2]]:
    """Mixin which allows the override of the filename being
    passed back to the user when the spreadsheet is downloaded.

    Args:
        assignee (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, TaskEventsListEvent]):
        event_in (Union[Unset, None, str]):
        field (Union[Unset, None, TaskEventsListField]):
        format_ (Union[Unset, None, TaskEventsListFormat]):
        from_state (Union[Unset, None, TaskEventsListFromState]):
        from_state_in (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        task (Union[Unset, None, str]):
        task_account (Union[Unset, None, str]):
        to_state (Union[Unset, None, TaskEventsListToState]):
        to_state_in (Union[Unset, None, str]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[TaskEventSerializerV2]]
    """

    kwargs = _get_kwargs(
        client=client,
        assignee=assignee,
        cursor=cursor,
        event=event,
        event_in=event_in,
        field=field,
        format_=format_,
        from_state=from_state,
        from_state_in=from_state_in,
        ordering=ordering,
        page_size=page_size,
        task=task,
        task_account=task_account,
        to_state=to_state,
        to_state_in=to_state_in,
        user=user,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    assignee: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    event: Union[Unset, None, TaskEventsListEvent] = UNSET,
    event_in: Union[Unset, None, str] = UNSET,
    field: Union[Unset, None, TaskEventsListField] = UNSET,
    format_: Union[Unset, None, TaskEventsListFormat] = UNSET,
    from_state: Union[Unset, None, TaskEventsListFromState] = UNSET,
    from_state_in: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    task_account: Union[Unset, None, str] = UNSET,
    to_state: Union[Unset, None, TaskEventsListToState] = UNSET,
    to_state_in: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Optional[List[TaskEventSerializerV2]]:
    """Mixin which allows the override of the filename being
    passed back to the user when the spreadsheet is downloaded.

    Args:
        assignee (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        event (Union[Unset, None, TaskEventsListEvent]):
        event_in (Union[Unset, None, str]):
        field (Union[Unset, None, TaskEventsListField]):
        format_ (Union[Unset, None, TaskEventsListFormat]):
        from_state (Union[Unset, None, TaskEventsListFromState]):
        from_state_in (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        task (Union[Unset, None, str]):
        task_account (Union[Unset, None, str]):
        to_state (Union[Unset, None, TaskEventsListToState]):
        to_state_in (Union[Unset, None, str]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[TaskEventSerializerV2]]
    """

    return (
        await asyncio_detailed(
            client=client,
            assignee=assignee,
            cursor=cursor,
            event=event,
            event_in=event_in,
            field=field,
            format_=format_,
            from_state=from_state,
            from_state_in=from_state_in,
            ordering=ordering,
            page_size=page_size,
            task=task,
            task_account=task_account,
            to_state=to_state,
            to_state_in=to_state_in,
            user=user,
        )
    ).parsed

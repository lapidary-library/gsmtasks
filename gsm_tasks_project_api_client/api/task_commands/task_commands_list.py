from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.task_command import TaskCommand
from ...models.task_commands_list_action import TaskCommandsListAction
from ...models.task_commands_list_format import TaskCommandsListFormat
from ...models.task_commands_list_state import TaskCommandsListState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    action: Union[Unset, None, TaskCommandsListAction] = UNSET,
    assignee: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, TaskCommandsListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, TaskCommandsListState] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    task_account: Union[Unset, None, str] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/task_commands/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_action: Union[Unset, None, str] = UNSET
    if not isinstance(action, Unset):
        json_action = action.value if action else None

    params["action"] = json_action

    params["assignee"] = assignee

    params["cursor"] = cursor

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["page_size"] = page_size

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params["task"] = task

    params["task__account"] = task_account

    params["time"] = time

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


def _parse_response(*, response: httpx.Response) -> Optional[List[TaskCommand]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_task_command_list_item_data in _response_200:
            componentsschemas_paginated_task_command_list_item = TaskCommand.from_dict(
                componentsschemas_paginated_task_command_list_item_data
            )

            response_200.append(componentsschemas_paginated_task_command_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[TaskCommand]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    action: Union[Unset, None, TaskCommandsListAction] = UNSET,
    assignee: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, TaskCommandsListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, TaskCommandsListState] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    task_account: Union[Unset, None, str] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Response[List[TaskCommand]]:
    """
    Args:
        action (Union[Unset, None, TaskCommandsListAction]):
        assignee (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, TaskCommandsListFormat]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, TaskCommandsListState]):
        task (Union[Unset, None, str]):
        task_account (Union[Unset, None, str]):
        time (Union[Unset, None, str]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[TaskCommand]]
    """

    kwargs = _get_kwargs(
        client=client,
        action=action,
        assignee=assignee,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
        state=state,
        task=task,
        task_account=task_account,
        time=time,
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
    action: Union[Unset, None, TaskCommandsListAction] = UNSET,
    assignee: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, TaskCommandsListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, TaskCommandsListState] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    task_account: Union[Unset, None, str] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Optional[List[TaskCommand]]:
    """
    Args:
        action (Union[Unset, None, TaskCommandsListAction]):
        assignee (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, TaskCommandsListFormat]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, TaskCommandsListState]):
        task (Union[Unset, None, str]):
        task_account (Union[Unset, None, str]):
        time (Union[Unset, None, str]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[TaskCommand]]
    """

    return sync_detailed(
        client=client,
        action=action,
        assignee=assignee,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
        state=state,
        task=task,
        task_account=task_account,
        time=time,
        user=user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    action: Union[Unset, None, TaskCommandsListAction] = UNSET,
    assignee: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, TaskCommandsListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, TaskCommandsListState] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    task_account: Union[Unset, None, str] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Response[List[TaskCommand]]:
    """
    Args:
        action (Union[Unset, None, TaskCommandsListAction]):
        assignee (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, TaskCommandsListFormat]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, TaskCommandsListState]):
        task (Union[Unset, None, str]):
        task_account (Union[Unset, None, str]):
        time (Union[Unset, None, str]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[TaskCommand]]
    """

    kwargs = _get_kwargs(
        client=client,
        action=action,
        assignee=assignee,
        cursor=cursor,
        format_=format_,
        page_size=page_size,
        state=state,
        task=task,
        task_account=task_account,
        time=time,
        user=user,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    action: Union[Unset, None, TaskCommandsListAction] = UNSET,
    assignee: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, TaskCommandsListFormat] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, TaskCommandsListState] = UNSET,
    task: Union[Unset, None, str] = UNSET,
    task_account: Union[Unset, None, str] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    user: Union[Unset, None, str] = UNSET,
) -> Optional[List[TaskCommand]]:
    """
    Args:
        action (Union[Unset, None, TaskCommandsListAction]):
        assignee (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, TaskCommandsListFormat]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, TaskCommandsListState]):
        task (Union[Unset, None, str]):
        task_account (Union[Unset, None, str]):
        time (Union[Unset, None, str]):
        user (Union[Unset, None, str]):

    Returns:
        Response[List[TaskCommand]]
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            assignee=assignee,
            cursor=cursor,
            format_=format_,
            page_size=page_size,
            state=state,
            task=task,
            task_account=task_account,
            time=time,
            user=user,
        )
    ).parsed

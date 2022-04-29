from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.task_list_reorder_request import TaskListReorderRequest
from ...models.tasks_reorder_create_format import TasksReorderCreateFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: TaskListReorderRequest,
    format_: Union[Unset, None, TasksReorderCreateFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/tasks/reorder/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[TaskListReorderRequest]:
    if response.status_code == 200:
        response_200 = TaskListReorderRequest.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[TaskListReorderRequest]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: TaskListReorderRequest,
    format_: Union[Unset, None, TasksReorderCreateFormat] = UNSET,
) -> Response[TaskListReorderRequest]:
    """
    Args:
        format_ (Union[Unset, None, TasksReorderCreateFormat]):
        json_body (TaskListReorderRequest):

    Returns:
        Response[TaskListReorderRequest]
    """

    kwargs = _get_kwargs(
        client=client,
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
    json_body: TaskListReorderRequest,
    format_: Union[Unset, None, TasksReorderCreateFormat] = UNSET,
) -> Optional[TaskListReorderRequest]:
    """
    Args:
        format_ (Union[Unset, None, TasksReorderCreateFormat]):
        json_body (TaskListReorderRequest):

    Returns:
        Response[TaskListReorderRequest]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: TaskListReorderRequest,
    format_: Union[Unset, None, TasksReorderCreateFormat] = UNSET,
) -> Response[TaskListReorderRequest]:
    """
    Args:
        format_ (Union[Unset, None, TasksReorderCreateFormat]):
        json_body (TaskListReorderRequest):

    Returns:
        Response[TaskListReorderRequest]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: TaskListReorderRequest,
    format_: Union[Unset, None, TasksReorderCreateFormat] = UNSET,
) -> Optional[TaskListReorderRequest]:
    """
    Args:
        format_ (Union[Unset, None, TasksReorderCreateFormat]):
        json_body (TaskListReorderRequest):

    Returns:
        Response[TaskListReorderRequest]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            format_=format_,
        )
    ).parsed

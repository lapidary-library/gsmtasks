from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.route_optimization_serializer_v2 import RouteOptimizationSerializerV2
from ...models.route_optimizations_list_format import RouteOptimizationsListFormat
from ...models.route_optimizations_list_objective import RouteOptimizationsListObjective
from ...models.route_optimizations_list_state import RouteOptimizationsListState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    assignees_id_in: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, RouteOptimizationsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    objective: Union[Unset, None, RouteOptimizationsListObjective] = UNSET,
    objective_in: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, RouteOptimizationsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    total_distance_gt: Union[Unset, None, str] = UNSET,
    total_distance_gte: Union[Unset, None, str] = UNSET,
    total_distance_lt: Union[Unset, None, str] = UNSET,
    total_distance_lte: Union[Unset, None, str] = UNSET,
    total_duration_gt: Union[Unset, None, str] = UNSET,
    total_duration_gte: Union[Unset, None, str] = UNSET,
    total_duration_lt: Union[Unset, None, str] = UNSET,
    total_duration_lte: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/route_optimizations/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["assignees__id__in"] = assignees_id_in

    params["cursor"] = cursor

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["id"] = id

    json_objective: Union[Unset, None, str] = UNSET
    if not isinstance(objective, Unset):
        json_objective = objective.value if objective else None

    params["objective"] = json_objective

    params["objective__in"] = objective_in

    params["ordering"] = ordering

    params["page_size"] = page_size

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params["state__in"] = state_in

    params["total_distance__gt"] = total_distance_gt

    params["total_distance__gte"] = total_distance_gte

    params["total_distance__lt"] = total_distance_lt

    params["total_distance__lte"] = total_distance_lte

    params["total_duration__gt"] = total_duration_gt

    params["total_duration__gte"] = total_duration_gte

    params["total_duration__lt"] = total_duration_lt

    params["total_duration__lte"] = total_duration_lte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[RouteOptimizationSerializerV2]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_route_optimization_serializer_v2_list_item_data in _response_200:
            componentsschemas_paginated_route_optimization_serializer_v2_list_item = (
                RouteOptimizationSerializerV2.from_dict(
                    componentsschemas_paginated_route_optimization_serializer_v2_list_item_data
                )
            )

            response_200.append(componentsschemas_paginated_route_optimization_serializer_v2_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[RouteOptimizationSerializerV2]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    assignees_id_in: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, RouteOptimizationsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    objective: Union[Unset, None, RouteOptimizationsListObjective] = UNSET,
    objective_in: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, RouteOptimizationsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    total_distance_gt: Union[Unset, None, str] = UNSET,
    total_distance_gte: Union[Unset, None, str] = UNSET,
    total_distance_lt: Union[Unset, None, str] = UNSET,
    total_distance_lte: Union[Unset, None, str] = UNSET,
    total_duration_gt: Union[Unset, None, str] = UNSET,
    total_duration_gte: Union[Unset, None, str] = UNSET,
    total_duration_lt: Union[Unset, None, str] = UNSET,
    total_duration_lte: Union[Unset, None, str] = UNSET,
) -> Response[List[RouteOptimizationSerializerV2]]:
    """
    Args:
        account (Union[Unset, None, str]):
        assignees_id_in (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, RouteOptimizationsListFormat]):
        id (Union[Unset, None, str]):
        objective (Union[Unset, None, RouteOptimizationsListObjective]):
        objective_in (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, RouteOptimizationsListState]):
        state_in (Union[Unset, None, str]):
        total_distance_gt (Union[Unset, None, str]):
        total_distance_gte (Union[Unset, None, str]):
        total_distance_lt (Union[Unset, None, str]):
        total_distance_lte (Union[Unset, None, str]):
        total_duration_gt (Union[Unset, None, str]):
        total_duration_gte (Union[Unset, None, str]):
        total_duration_lt (Union[Unset, None, str]):
        total_duration_lte (Union[Unset, None, str]):

    Returns:
        Response[List[RouteOptimizationSerializerV2]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        assignees_id_in=assignees_id_in,
        cursor=cursor,
        format_=format_,
        id=id,
        objective=objective,
        objective_in=objective_in,
        ordering=ordering,
        page_size=page_size,
        state=state,
        state_in=state_in,
        total_distance_gt=total_distance_gt,
        total_distance_gte=total_distance_gte,
        total_distance_lt=total_distance_lt,
        total_distance_lte=total_distance_lte,
        total_duration_gt=total_duration_gt,
        total_duration_gte=total_duration_gte,
        total_duration_lt=total_duration_lt,
        total_duration_lte=total_duration_lte,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    assignees_id_in: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, RouteOptimizationsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    objective: Union[Unset, None, RouteOptimizationsListObjective] = UNSET,
    objective_in: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, RouteOptimizationsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    total_distance_gt: Union[Unset, None, str] = UNSET,
    total_distance_gte: Union[Unset, None, str] = UNSET,
    total_distance_lt: Union[Unset, None, str] = UNSET,
    total_distance_lte: Union[Unset, None, str] = UNSET,
    total_duration_gt: Union[Unset, None, str] = UNSET,
    total_duration_gte: Union[Unset, None, str] = UNSET,
    total_duration_lt: Union[Unset, None, str] = UNSET,
    total_duration_lte: Union[Unset, None, str] = UNSET,
) -> Optional[List[RouteOptimizationSerializerV2]]:
    """
    Args:
        account (Union[Unset, None, str]):
        assignees_id_in (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, RouteOptimizationsListFormat]):
        id (Union[Unset, None, str]):
        objective (Union[Unset, None, RouteOptimizationsListObjective]):
        objective_in (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, RouteOptimizationsListState]):
        state_in (Union[Unset, None, str]):
        total_distance_gt (Union[Unset, None, str]):
        total_distance_gte (Union[Unset, None, str]):
        total_distance_lt (Union[Unset, None, str]):
        total_distance_lte (Union[Unset, None, str]):
        total_duration_gt (Union[Unset, None, str]):
        total_duration_gte (Union[Unset, None, str]):
        total_duration_lt (Union[Unset, None, str]):
        total_duration_lte (Union[Unset, None, str]):

    Returns:
        Response[List[RouteOptimizationSerializerV2]]
    """

    return sync_detailed(
        client=client,
        account=account,
        assignees_id_in=assignees_id_in,
        cursor=cursor,
        format_=format_,
        id=id,
        objective=objective,
        objective_in=objective_in,
        ordering=ordering,
        page_size=page_size,
        state=state,
        state_in=state_in,
        total_distance_gt=total_distance_gt,
        total_distance_gte=total_distance_gte,
        total_distance_lt=total_distance_lt,
        total_distance_lte=total_distance_lte,
        total_duration_gt=total_duration_gt,
        total_duration_gte=total_duration_gte,
        total_duration_lt=total_duration_lt,
        total_duration_lte=total_duration_lte,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    assignees_id_in: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, RouteOptimizationsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    objective: Union[Unset, None, RouteOptimizationsListObjective] = UNSET,
    objective_in: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, RouteOptimizationsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    total_distance_gt: Union[Unset, None, str] = UNSET,
    total_distance_gte: Union[Unset, None, str] = UNSET,
    total_distance_lt: Union[Unset, None, str] = UNSET,
    total_distance_lte: Union[Unset, None, str] = UNSET,
    total_duration_gt: Union[Unset, None, str] = UNSET,
    total_duration_gte: Union[Unset, None, str] = UNSET,
    total_duration_lt: Union[Unset, None, str] = UNSET,
    total_duration_lte: Union[Unset, None, str] = UNSET,
) -> Response[List[RouteOptimizationSerializerV2]]:
    """
    Args:
        account (Union[Unset, None, str]):
        assignees_id_in (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, RouteOptimizationsListFormat]):
        id (Union[Unset, None, str]):
        objective (Union[Unset, None, RouteOptimizationsListObjective]):
        objective_in (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, RouteOptimizationsListState]):
        state_in (Union[Unset, None, str]):
        total_distance_gt (Union[Unset, None, str]):
        total_distance_gte (Union[Unset, None, str]):
        total_distance_lt (Union[Unset, None, str]):
        total_distance_lte (Union[Unset, None, str]):
        total_duration_gt (Union[Unset, None, str]):
        total_duration_gte (Union[Unset, None, str]):
        total_duration_lt (Union[Unset, None, str]):
        total_duration_lte (Union[Unset, None, str]):

    Returns:
        Response[List[RouteOptimizationSerializerV2]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        assignees_id_in=assignees_id_in,
        cursor=cursor,
        format_=format_,
        id=id,
        objective=objective,
        objective_in=objective_in,
        ordering=ordering,
        page_size=page_size,
        state=state,
        state_in=state_in,
        total_distance_gt=total_distance_gt,
        total_distance_gte=total_distance_gte,
        total_distance_lt=total_distance_lt,
        total_distance_lte=total_distance_lte,
        total_duration_gt=total_duration_gt,
        total_duration_gte=total_duration_gte,
        total_duration_lt=total_duration_lt,
        total_duration_lte=total_duration_lte,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    assignees_id_in: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, RouteOptimizationsListFormat] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    objective: Union[Unset, None, RouteOptimizationsListObjective] = UNSET,
    objective_in: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    state: Union[Unset, None, RouteOptimizationsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    total_distance_gt: Union[Unset, None, str] = UNSET,
    total_distance_gte: Union[Unset, None, str] = UNSET,
    total_distance_lt: Union[Unset, None, str] = UNSET,
    total_distance_lte: Union[Unset, None, str] = UNSET,
    total_duration_gt: Union[Unset, None, str] = UNSET,
    total_duration_gte: Union[Unset, None, str] = UNSET,
    total_duration_lt: Union[Unset, None, str] = UNSET,
    total_duration_lte: Union[Unset, None, str] = UNSET,
) -> Optional[List[RouteOptimizationSerializerV2]]:
    """
    Args:
        account (Union[Unset, None, str]):
        assignees_id_in (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, RouteOptimizationsListFormat]):
        id (Union[Unset, None, str]):
        objective (Union[Unset, None, RouteOptimizationsListObjective]):
        objective_in (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        state (Union[Unset, None, RouteOptimizationsListState]):
        state_in (Union[Unset, None, str]):
        total_distance_gt (Union[Unset, None, str]):
        total_distance_gte (Union[Unset, None, str]):
        total_distance_lt (Union[Unset, None, str]):
        total_distance_lte (Union[Unset, None, str]):
        total_duration_gt (Union[Unset, None, str]):
        total_duration_gte (Union[Unset, None, str]):
        total_duration_lt (Union[Unset, None, str]):
        total_duration_lte (Union[Unset, None, str]):

    Returns:
        Response[List[RouteOptimizationSerializerV2]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            assignees_id_in=assignees_id_in,
            cursor=cursor,
            format_=format_,
            id=id,
            objective=objective,
            objective_in=objective_in,
            ordering=ordering,
            page_size=page_size,
            state=state,
            state_in=state_in,
            total_distance_gt=total_distance_gt,
            total_distance_gte=total_distance_gte,
            total_distance_lt=total_distance_lt,
            total_distance_lte=total_distance_lte,
            total_duration_gt=total_duration_gt,
            total_duration_gte=total_duration_gte,
            total_duration_lt=total_duration_lt,
            total_duration_lte=total_duration_lte,
        )
    ).parsed

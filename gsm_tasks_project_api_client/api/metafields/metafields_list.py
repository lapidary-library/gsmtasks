from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.metafield import Metafield
from ...models.metafields_list_format import MetafieldsListFormat
from ...models.metafields_list_value_type import MetafieldsListValueType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, MetafieldsListFormat] = UNSET,
    is_editable: Union[Unset, None, str] = UNSET,
    is_editable_assignee: Union[Unset, None, str] = UNSET,
    is_persistent: Union[Unset, None, str] = UNSET,
    is_required: Union[Unset, None, str] = UNSET,
    is_searchable: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    label: Union[Unset, None, str] = UNSET,
    namespace: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    show_in_detail_view: Union[Unset, None, str] = UNSET,
    show_in_list_view: Union[Unset, None, str] = UNSET,
    show_in_mobile_app: Union[Unset, None, str] = UNSET,
    show_in_pod: Union[Unset, None, str] = UNSET,
    show_when_task_type_assignment: Union[Unset, None, str] = UNSET,
    show_when_task_type_drop_off: Union[Unset, None, str] = UNSET,
    show_when_task_type_pick_up: Union[Unset, None, str] = UNSET,
    value_type: Union[Unset, None, MetafieldsListValueType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/metafields/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["cursor"] = cursor

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["is_editable"] = is_editable

    params["is_editable_assignee"] = is_editable_assignee

    params["is_persistent"] = is_persistent

    params["is_required"] = is_required

    params["is_searchable"] = is_searchable

    params["key"] = key

    params["label"] = label

    params["namespace"] = namespace

    params["ordering"] = ordering

    params["page_size"] = page_size

    params["search"] = search

    params["show_in_detail_view"] = show_in_detail_view

    params["show_in_list_view"] = show_in_list_view

    params["show_in_mobile_app"] = show_in_mobile_app

    params["show_in_pod"] = show_in_pod

    params["show_when_task_type_assignment"] = show_when_task_type_assignment

    params["show_when_task_type_drop_off"] = show_when_task_type_drop_off

    params["show_when_task_type_pick_up"] = show_when_task_type_pick_up

    json_value_type: Union[Unset, None, str] = UNSET
    if not isinstance(value_type, Unset):
        json_value_type = value_type.value if value_type else None

    params["value_type"] = json_value_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Metafield]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_metafield_list_item_data in _response_200:
            componentsschemas_paginated_metafield_list_item = Metafield.from_dict(
                componentsschemas_paginated_metafield_list_item_data
            )

            response_200.append(componentsschemas_paginated_metafield_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Metafield]]:
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
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, MetafieldsListFormat] = UNSET,
    is_editable: Union[Unset, None, str] = UNSET,
    is_editable_assignee: Union[Unset, None, str] = UNSET,
    is_persistent: Union[Unset, None, str] = UNSET,
    is_required: Union[Unset, None, str] = UNSET,
    is_searchable: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    label: Union[Unset, None, str] = UNSET,
    namespace: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    show_in_detail_view: Union[Unset, None, str] = UNSET,
    show_in_list_view: Union[Unset, None, str] = UNSET,
    show_in_mobile_app: Union[Unset, None, str] = UNSET,
    show_in_pod: Union[Unset, None, str] = UNSET,
    show_when_task_type_assignment: Union[Unset, None, str] = UNSET,
    show_when_task_type_drop_off: Union[Unset, None, str] = UNSET,
    show_when_task_type_pick_up: Union[Unset, None, str] = UNSET,
    value_type: Union[Unset, None, MetafieldsListValueType] = UNSET,
) -> Response[List[Metafield]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, MetafieldsListFormat]):
        is_editable (Union[Unset, None, str]):
        is_editable_assignee (Union[Unset, None, str]):
        is_persistent (Union[Unset, None, str]):
        is_required (Union[Unset, None, str]):
        is_searchable (Union[Unset, None, str]):
        key (Union[Unset, None, str]):
        label (Union[Unset, None, str]):
        namespace (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        show_in_detail_view (Union[Unset, None, str]):
        show_in_list_view (Union[Unset, None, str]):
        show_in_mobile_app (Union[Unset, None, str]):
        show_in_pod (Union[Unset, None, str]):
        show_when_task_type_assignment (Union[Unset, None, str]):
        show_when_task_type_drop_off (Union[Unset, None, str]):
        show_when_task_type_pick_up (Union[Unset, None, str]):
        value_type (Union[Unset, None, MetafieldsListValueType]):

    Returns:
        Response[List[Metafield]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        format_=format_,
        is_editable=is_editable,
        is_editable_assignee=is_editable_assignee,
        is_persistent=is_persistent,
        is_required=is_required,
        is_searchable=is_searchable,
        key=key,
        label=label,
        namespace=namespace,
        ordering=ordering,
        page_size=page_size,
        search=search,
        show_in_detail_view=show_in_detail_view,
        show_in_list_view=show_in_list_view,
        show_in_mobile_app=show_in_mobile_app,
        show_in_pod=show_in_pod,
        show_when_task_type_assignment=show_when_task_type_assignment,
        show_when_task_type_drop_off=show_when_task_type_drop_off,
        show_when_task_type_pick_up=show_when_task_type_pick_up,
        value_type=value_type,
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
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, MetafieldsListFormat] = UNSET,
    is_editable: Union[Unset, None, str] = UNSET,
    is_editable_assignee: Union[Unset, None, str] = UNSET,
    is_persistent: Union[Unset, None, str] = UNSET,
    is_required: Union[Unset, None, str] = UNSET,
    is_searchable: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    label: Union[Unset, None, str] = UNSET,
    namespace: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    show_in_detail_view: Union[Unset, None, str] = UNSET,
    show_in_list_view: Union[Unset, None, str] = UNSET,
    show_in_mobile_app: Union[Unset, None, str] = UNSET,
    show_in_pod: Union[Unset, None, str] = UNSET,
    show_when_task_type_assignment: Union[Unset, None, str] = UNSET,
    show_when_task_type_drop_off: Union[Unset, None, str] = UNSET,
    show_when_task_type_pick_up: Union[Unset, None, str] = UNSET,
    value_type: Union[Unset, None, MetafieldsListValueType] = UNSET,
) -> Optional[List[Metafield]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, MetafieldsListFormat]):
        is_editable (Union[Unset, None, str]):
        is_editable_assignee (Union[Unset, None, str]):
        is_persistent (Union[Unset, None, str]):
        is_required (Union[Unset, None, str]):
        is_searchable (Union[Unset, None, str]):
        key (Union[Unset, None, str]):
        label (Union[Unset, None, str]):
        namespace (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        show_in_detail_view (Union[Unset, None, str]):
        show_in_list_view (Union[Unset, None, str]):
        show_in_mobile_app (Union[Unset, None, str]):
        show_in_pod (Union[Unset, None, str]):
        show_when_task_type_assignment (Union[Unset, None, str]):
        show_when_task_type_drop_off (Union[Unset, None, str]):
        show_when_task_type_pick_up (Union[Unset, None, str]):
        value_type (Union[Unset, None, MetafieldsListValueType]):

    Returns:
        Response[List[Metafield]]
    """

    return sync_detailed(
        client=client,
        account=account,
        cursor=cursor,
        format_=format_,
        is_editable=is_editable,
        is_editable_assignee=is_editable_assignee,
        is_persistent=is_persistent,
        is_required=is_required,
        is_searchable=is_searchable,
        key=key,
        label=label,
        namespace=namespace,
        ordering=ordering,
        page_size=page_size,
        search=search,
        show_in_detail_view=show_in_detail_view,
        show_in_list_view=show_in_list_view,
        show_in_mobile_app=show_in_mobile_app,
        show_in_pod=show_in_pod,
        show_when_task_type_assignment=show_when_task_type_assignment,
        show_when_task_type_drop_off=show_when_task_type_drop_off,
        show_when_task_type_pick_up=show_when_task_type_pick_up,
        value_type=value_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, MetafieldsListFormat] = UNSET,
    is_editable: Union[Unset, None, str] = UNSET,
    is_editable_assignee: Union[Unset, None, str] = UNSET,
    is_persistent: Union[Unset, None, str] = UNSET,
    is_required: Union[Unset, None, str] = UNSET,
    is_searchable: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    label: Union[Unset, None, str] = UNSET,
    namespace: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    show_in_detail_view: Union[Unset, None, str] = UNSET,
    show_in_list_view: Union[Unset, None, str] = UNSET,
    show_in_mobile_app: Union[Unset, None, str] = UNSET,
    show_in_pod: Union[Unset, None, str] = UNSET,
    show_when_task_type_assignment: Union[Unset, None, str] = UNSET,
    show_when_task_type_drop_off: Union[Unset, None, str] = UNSET,
    show_when_task_type_pick_up: Union[Unset, None, str] = UNSET,
    value_type: Union[Unset, None, MetafieldsListValueType] = UNSET,
) -> Response[List[Metafield]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, MetafieldsListFormat]):
        is_editable (Union[Unset, None, str]):
        is_editable_assignee (Union[Unset, None, str]):
        is_persistent (Union[Unset, None, str]):
        is_required (Union[Unset, None, str]):
        is_searchable (Union[Unset, None, str]):
        key (Union[Unset, None, str]):
        label (Union[Unset, None, str]):
        namespace (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        show_in_detail_view (Union[Unset, None, str]):
        show_in_list_view (Union[Unset, None, str]):
        show_in_mobile_app (Union[Unset, None, str]):
        show_in_pod (Union[Unset, None, str]):
        show_when_task_type_assignment (Union[Unset, None, str]):
        show_when_task_type_drop_off (Union[Unset, None, str]):
        show_when_task_type_pick_up (Union[Unset, None, str]):
        value_type (Union[Unset, None, MetafieldsListValueType]):

    Returns:
        Response[List[Metafield]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        format_=format_,
        is_editable=is_editable,
        is_editable_assignee=is_editable_assignee,
        is_persistent=is_persistent,
        is_required=is_required,
        is_searchable=is_searchable,
        key=key,
        label=label,
        namespace=namespace,
        ordering=ordering,
        page_size=page_size,
        search=search,
        show_in_detail_view=show_in_detail_view,
        show_in_list_view=show_in_list_view,
        show_in_mobile_app=show_in_mobile_app,
        show_in_pod=show_in_pod,
        show_when_task_type_assignment=show_when_task_type_assignment,
        show_when_task_type_drop_off=show_when_task_type_drop_off,
        show_when_task_type_pick_up=show_when_task_type_pick_up,
        value_type=value_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, MetafieldsListFormat] = UNSET,
    is_editable: Union[Unset, None, str] = UNSET,
    is_editable_assignee: Union[Unset, None, str] = UNSET,
    is_persistent: Union[Unset, None, str] = UNSET,
    is_required: Union[Unset, None, str] = UNSET,
    is_searchable: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    label: Union[Unset, None, str] = UNSET,
    namespace: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    show_in_detail_view: Union[Unset, None, str] = UNSET,
    show_in_list_view: Union[Unset, None, str] = UNSET,
    show_in_mobile_app: Union[Unset, None, str] = UNSET,
    show_in_pod: Union[Unset, None, str] = UNSET,
    show_when_task_type_assignment: Union[Unset, None, str] = UNSET,
    show_when_task_type_drop_off: Union[Unset, None, str] = UNSET,
    show_when_task_type_pick_up: Union[Unset, None, str] = UNSET,
    value_type: Union[Unset, None, MetafieldsListValueType] = UNSET,
) -> Optional[List[Metafield]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, MetafieldsListFormat]):
        is_editable (Union[Unset, None, str]):
        is_editable_assignee (Union[Unset, None, str]):
        is_persistent (Union[Unset, None, str]):
        is_required (Union[Unset, None, str]):
        is_searchable (Union[Unset, None, str]):
        key (Union[Unset, None, str]):
        label (Union[Unset, None, str]):
        namespace (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        show_in_detail_view (Union[Unset, None, str]):
        show_in_list_view (Union[Unset, None, str]):
        show_in_mobile_app (Union[Unset, None, str]):
        show_in_pod (Union[Unset, None, str]):
        show_when_task_type_assignment (Union[Unset, None, str]):
        show_when_task_type_drop_off (Union[Unset, None, str]):
        show_when_task_type_pick_up (Union[Unset, None, str]):
        value_type (Union[Unset, None, MetafieldsListValueType]):

    Returns:
        Response[List[Metafield]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            cursor=cursor,
            format_=format_,
            is_editable=is_editable,
            is_editable_assignee=is_editable_assignee,
            is_persistent=is_persistent,
            is_required=is_required,
            is_searchable=is_searchable,
            key=key,
            label=label,
            namespace=namespace,
            ordering=ordering,
            page_size=page_size,
            search=search,
            show_in_detail_view=show_in_detail_view,
            show_in_list_view=show_in_list_view,
            show_in_mobile_app=show_in_mobile_app,
            show_in_pod=show_in_pod,
            show_when_task_type_assignment=show_when_task_type_assignment,
            show_when_task_type_drop_off=show_when_task_type_drop_off,
            show_when_task_type_pick_up=show_when_task_type_pick_up,
            value_type=value_type,
        )
    ).parsed

from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.email import Email
from ...models.emails_list_format import EmailsListFormat
from ...models.emails_list_state import EmailsListState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, EmailsListFormat] = UNSET,
    from_email: Union[Unset, None, str] = UNSET,
    from_email_icontains: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    reply_to_email: Union[Unset, None, str] = UNSET,
    reply_to_email_icontains: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, EmailsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    subject_icontains: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/emails/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["cursor"] = cursor

    params["external_id"] = external_id

    params["external_id__icontains"] = external_id_icontains

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["from_email"] = from_email

    params["from_email__icontains"] = from_email_icontains

    params["id"] = id

    params["message"] = message

    params["message__icontains"] = message_icontains

    params["ordering"] = ordering

    params["page_size"] = page_size

    params["reply_to_email"] = reply_to_email

    params["reply_to_email__icontains"] = reply_to_email_icontains

    params["search"] = search

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params["state__in"] = state_in

    params["subject"] = subject

    params["subject__icontains"] = subject_icontains

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Email]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_email_list_item_data in _response_200:
            componentsschemas_paginated_email_list_item = Email.from_dict(
                componentsschemas_paginated_email_list_item_data
            )

            response_200.append(componentsschemas_paginated_email_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Email]]:
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
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, EmailsListFormat] = UNSET,
    from_email: Union[Unset, None, str] = UNSET,
    from_email_icontains: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    reply_to_email: Union[Unset, None, str] = UNSET,
    reply_to_email_icontains: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, EmailsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    subject_icontains: Union[Unset, None, str] = UNSET,
) -> Response[List[Email]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        external_id (Union[Unset, None, str]):
        external_id_icontains (Union[Unset, None, str]):
        format_ (Union[Unset, None, EmailsListFormat]):
        from_email (Union[Unset, None, str]):
        from_email_icontains (Union[Unset, None, str]):
        id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        message_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        reply_to_email (Union[Unset, None, str]):
        reply_to_email_icontains (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, EmailsListState]):
        state_in (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        subject_icontains (Union[Unset, None, str]):

    Returns:
        Response[List[Email]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        external_id=external_id,
        external_id_icontains=external_id_icontains,
        format_=format_,
        from_email=from_email,
        from_email_icontains=from_email_icontains,
        id=id,
        message=message,
        message_icontains=message_icontains,
        ordering=ordering,
        page_size=page_size,
        reply_to_email=reply_to_email,
        reply_to_email_icontains=reply_to_email_icontains,
        search=search,
        state=state,
        state_in=state_in,
        subject=subject,
        subject_icontains=subject_icontains,
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
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, EmailsListFormat] = UNSET,
    from_email: Union[Unset, None, str] = UNSET,
    from_email_icontains: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    reply_to_email: Union[Unset, None, str] = UNSET,
    reply_to_email_icontains: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, EmailsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    subject_icontains: Union[Unset, None, str] = UNSET,
) -> Optional[List[Email]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        external_id (Union[Unset, None, str]):
        external_id_icontains (Union[Unset, None, str]):
        format_ (Union[Unset, None, EmailsListFormat]):
        from_email (Union[Unset, None, str]):
        from_email_icontains (Union[Unset, None, str]):
        id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        message_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        reply_to_email (Union[Unset, None, str]):
        reply_to_email_icontains (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, EmailsListState]):
        state_in (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        subject_icontains (Union[Unset, None, str]):

    Returns:
        Response[List[Email]]
    """

    return sync_detailed(
        client=client,
        account=account,
        cursor=cursor,
        external_id=external_id,
        external_id_icontains=external_id_icontains,
        format_=format_,
        from_email=from_email,
        from_email_icontains=from_email_icontains,
        id=id,
        message=message,
        message_icontains=message_icontains,
        ordering=ordering,
        page_size=page_size,
        reply_to_email=reply_to_email,
        reply_to_email_icontains=reply_to_email_icontains,
        search=search,
        state=state,
        state_in=state_in,
        subject=subject,
        subject_icontains=subject_icontains,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, EmailsListFormat] = UNSET,
    from_email: Union[Unset, None, str] = UNSET,
    from_email_icontains: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    reply_to_email: Union[Unset, None, str] = UNSET,
    reply_to_email_icontains: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, EmailsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    subject_icontains: Union[Unset, None, str] = UNSET,
) -> Response[List[Email]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        external_id (Union[Unset, None, str]):
        external_id_icontains (Union[Unset, None, str]):
        format_ (Union[Unset, None, EmailsListFormat]):
        from_email (Union[Unset, None, str]):
        from_email_icontains (Union[Unset, None, str]):
        id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        message_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        reply_to_email (Union[Unset, None, str]):
        reply_to_email_icontains (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, EmailsListState]):
        state_in (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        subject_icontains (Union[Unset, None, str]):

    Returns:
        Response[List[Email]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        cursor=cursor,
        external_id=external_id,
        external_id_icontains=external_id_icontains,
        format_=format_,
        from_email=from_email,
        from_email_icontains=from_email_icontains,
        id=id,
        message=message,
        message_icontains=message_icontains,
        ordering=ordering,
        page_size=page_size,
        reply_to_email=reply_to_email,
        reply_to_email_icontains=reply_to_email_icontains,
        search=search,
        state=state,
        state_in=state_in,
        subject=subject,
        subject_icontains=subject_icontains,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    external_id: Union[Unset, None, str] = UNSET,
    external_id_icontains: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, EmailsListFormat] = UNSET,
    from_email: Union[Unset, None, str] = UNSET,
    from_email_icontains: Union[Unset, None, str] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    message: Union[Unset, None, str] = UNSET,
    message_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    reply_to_email: Union[Unset, None, str] = UNSET,
    reply_to_email_icontains: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, EmailsListState] = UNSET,
    state_in: Union[Unset, None, str] = UNSET,
    subject: Union[Unset, None, str] = UNSET,
    subject_icontains: Union[Unset, None, str] = UNSET,
) -> Optional[List[Email]]:
    """
    Args:
        account (Union[Unset, None, str]):
        cursor (Union[Unset, None, int]):
        external_id (Union[Unset, None, str]):
        external_id_icontains (Union[Unset, None, str]):
        format_ (Union[Unset, None, EmailsListFormat]):
        from_email (Union[Unset, None, str]):
        from_email_icontains (Union[Unset, None, str]):
        id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        message_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        reply_to_email (Union[Unset, None, str]):
        reply_to_email_icontains (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        state (Union[Unset, None, EmailsListState]):
        state_in (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        subject_icontains (Union[Unset, None, str]):

    Returns:
        Response[List[Email]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            cursor=cursor,
            external_id=external_id,
            external_id_icontains=external_id_icontains,
            format_=format_,
            from_email=from_email,
            from_email_icontains=from_email_icontains,
            id=id,
            message=message,
            message_icontains=message_icontains,
            ordering=ordering,
            page_size=page_size,
            reply_to_email=reply_to_email,
            reply_to_email_icontains=reply_to_email_icontains,
            search=search,
            state=state,
            state_in=state_in,
            subject=subject,
            subject_icontains=subject_icontains,
        )
    ).parsed

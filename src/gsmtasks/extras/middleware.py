import typing

import httpx
from lapidary.runtime import Next


def _select_accept(request: httpx.Request) -> str | None:
    accept_arr = request.headers.get_list('Accept')
    if not accept_arr or len(accept_arr) == 1:
        return None
    else:
        return typing.cast(str, max(accept_arr, key=len))


async def fix_accept(request: httpx.Request, next_: Next) -> httpx.Response:
    if accept := _select_accept(request):
        request.headers['Accept'] = accept

    return await next_(request)

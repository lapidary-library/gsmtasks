import httpx
from lapidary.runtime import HttpxMiddleware


class MediaFixer(HttpxMiddleware[str|None]):
    async def handle_request(self, request: httpx.Request) -> str|None:
        accept_arr = request.headers.get_list('Accept')
        if len(accept_arr)==0:
            return None
        elif len(accept_arr)==1:
            return accept_arr[0]
        else:
            accept = max(accept_arr, key=len)
            request.headers['Accept'] = accept
            return accept


    async def handle_response(self, response: httpx.Response, request: httpx.Request, state: str|None) -> None:
        if state:
            response.headers['Content-Type'] = state

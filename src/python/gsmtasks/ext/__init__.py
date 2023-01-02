from collections.abc import Generator

import httpx
from lapidary.runtime.model.plugins import PagingPlugin


class GsmTasksPagingPlugin(PagingPlugin):
    def page_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        while True:
            response: httpx.Response = yield request
            next_url = response.links.get('next')
            if not next_url:
                return
            request = httpx.Request(request.method, next_url['url'], headers=request.headers)

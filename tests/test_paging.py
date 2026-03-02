import logging
import os

import pytest
from lapidary.runtime import with_auth

from gsmtasks import ApiClient
from gsmtasks.extras import fix_accept, iter_pages
from gsmtasks.components import securitySchemes

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


@pytest.mark.asyncio
async def test_paged_result():
    client = with_auth(ApiClient(middlewares=[fix_accept]), securitySchemes.api_key_tokenAuth(f"Token {os.environ['GSM_TASKS_TOKEN']}"))

    count = 0
    async for body, meta in iter_pages(client.tasks_list)(page_size_q=10):
        count += 1
        if count >= 13:
            break
    assert count == 13

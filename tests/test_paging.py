import logging
import os

import pytest

from gsmtasks import ApiClient
from gsmtasks.paging import iter_pages, next_link_cursor_extractor
from gsmtasks.components import securitySchemes

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


@pytest.mark.asyncio
async def test_paged_result():
    async with ApiClient() as client:
        client.lapidary_authenticate(securitySchemes.api_key_tokenAuth(f"Token {os.environ['GSM_TASKS_TOKEN']}"))
        count = 0
        async for body, meta in iter_pages(client.tasks_list)(page_size_q=10):
            print(body[0].url)
            count += 1
            if count >= 13:
                break
        assert count == 13

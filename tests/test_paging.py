import logging
import os
from collections.abc import AsyncIterator

import pytest

from gsmtasks import ApiClient
from gsmtasks.components import securitySchemes

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


@pytest.mark.skip
@pytest.mark.asyncio
async def test_paged_result(self):
    async with ApiClient() as client:
        client.lapidary_authenticate(securitySchemes.api_key_tokenAuth(f"Token {os.environ['GSM_TASKS_TOKEN']}"))
        result = await client.tasks_list(page_size_q=10)
        assert isinstance(result, AsyncIterator)

        # loop over 12 elements to force retrieving the next page
        x = 0
        async for elem in result:
            print(x, elem)
            if (x := x + 1) > 12:
                break
        self.assertEqual(13, x)

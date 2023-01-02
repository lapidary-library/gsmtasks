import logging
import os
import unittest
from collections.abc import AsyncIterator

from lapidary.runtime import auth

from gsmtasks.client import ApiClient, Auth

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


class PagingTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_paged_result(self):
        async with ApiClient(auth=Auth(tokenAuth=auth.HTTP(os.environ['GSM_TASKS_TOKEN']))) as client:
            result = await client.tasks_list(q_page_size=10)
            assert isinstance(result, AsyncIterator)

            # loop over 12 elements to force retrieving the next page
            x = 0
            async for elem in result:
                print(x, elem)
                if (x := x + 1) > 12:
                    break
            self.assertEqual(13, x)

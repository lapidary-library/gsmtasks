import logging
import os
import unittest

from lapidary.runtime import auth

from gsmtasks import ApiClient, Auth

logging.basicConfig()
logging.getLogger('lapidary').setLevel(logging.INFO)


class MyTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_something(self):
        async with ApiClient(auth=Auth(tokenAuth=auth.HTTP(os.environ['GSM_TASKS_TOKEN']))) as client:
            await client.accounts_list()

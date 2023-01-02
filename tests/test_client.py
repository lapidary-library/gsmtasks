import logging
import os
import uuid
from typing import cast
from unittest import IsolatedAsyncioTestCase
from uuid import UUID

import pytest
from lapidary.runtime import auth

from gsmtasks.client import Auth, ApiClient
from gsmtasks.components.schemas.account import Account
from gsmtasks.components.schemas.gsm_tasks_error import GSMTasksError

logging.basicConfig()
logging.getLogger('lapidary').setLevel(logging.INFO)


class ClientTest(IsolatedAsyncioTestCase):

    async def asyncSetUp(self) -> None:
        self.client = ApiClient(auth=Auth(tokenAuth=auth.HTTP(os.environ['GSM_TASKS_TOKEN'])))

    async def asyncTearDown(self) -> None:
        await self.client.__aexit__()

    async def test_single_param_query(self) -> None:
        response: list[Account] = await self.client.accounts_list(q_page_size=1)
        self.assertEqual(len(response), 1)

        account_id = cast(uuid.UUID, response[0].id)
        response2 = await self.client.accounts_retrieve(p_id=account_id)
        self.assertEqual(response2.id, account_id)

    async def test_invalid_token_raises(self):
        async with ApiClient(auth=Auth(tokenAuth=auth.HTTP('7'))) as bad_client:
            with self.assertRaises(GSMTasksError):
                await bad_client.accounts_list(q_page_size=1)

    async def test_task_metadata(self):
        await self.client.tasks_retrieve(p_id=UUID(hex='c3a0b9e4-df2b-44c4-b879-c0961dfc3620'))


@pytest.mark.asyncio
async def test_simple_call():
    async with ApiClient(auth=Auth(tokenAuth=auth.HTTP(os.environ['GSM_TASKS_TOKEN']))) as client:
        await client.accounts_list()

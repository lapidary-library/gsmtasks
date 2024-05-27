import logging
import os
import uuid
from typing import cast
from unittest import IsolatedAsyncioTestCase
from uuid import UUID

import pytest

from gsmtasks.client import ApiClient
from gsmtasks.components.schemas.Account.schema import Account
from gsmtasks.components.schemas.GSMTasksError.schema import GSMTasksError
from gsmtasks.components.securitySchemes import api_key_tokenAuth

logging.basicConfig()
logging.getLogger('lapidary').setLevel(logging.INFO)


class ClientTest(IsolatedAsyncioTestCase):

    async def asyncSetUp(self) -> None:
        self.client = ApiClient()
        self.client.lapidary_authenticate(api_key_tokenAuth(os.environ['GSM_TASKS_TOKEN']))

    async def asyncTearDown(self) -> None:
        await self.client.__aexit__()

    async def test_single_param_query(self) -> None:
        response: list[Account] = await self.client.accounts_list(q_page_size=1)
        self.assertEqual(len(response), 1)

        account_id = cast(uuid.UUID, response[0].id)
        response2 = await self.client.accounts_retrieve(p_id=account_id)
        self.assertEqual(response2.id, account_id)

    async def test_invalid_token_raises(self):
        client = ApiClient()
        client.lapidary_authenticate(api_key_tokenAuth('7'))

        async with client as bad_client:
            with self.assertRaises(GSMTasksError):
                await bad_client.accounts_list(q_page_size=1)

    async def test_task_metadata(self):
        await self.client.tasks_retrieve(p_id=UUID(hex='c3a0b9e4-df2b-44c4-b879-c0961dfc3620'))


@pytest.mark.asyncio
async def test_simple_call():
    client = ApiClient()
    client.lapidary_authenticate(api_key_tokenAuth(os.environ['GSM_TASKS_TOKEN']))
    async with client:
        await client.accounts_list()

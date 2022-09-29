import logging
import os
import sys
from pprint import pp
from unittest import IsolatedAsyncioTestCase
from uuid import UUID

from gen.gsmtasks.components.schemas.task import Task
from gsmtasks.client import ApiClient
from gsmtasks.components.schemas.account import Account
from gsmtasks.components.schemas.gsm_tasks_error import GSMTasksError

logging.basicConfig()


class ClientTest(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        logging.getLogger('lapidary_base').setLevel(logging.DEBUG)
        self.client = ApiClient(os.environ['GSM_TASKS_TOKEN'])

    async def asyncTearDown(self) -> None:
        await self.client._client.__aexit__()

    async def test_single_param_query(self):
        response: list[Account] = await self.client.accounts_list(q_page_size=1)
        dicts = [task.dict(exclude_none=True, exclude_unset=True) for task in response]
        pp(dicts, stream=sys.stderr)
        self.assertEqual(len(response), 1)

        account_id = response[0].id
        response2 = await self.client.accounts_retrieve(p_id=account_id)
        self.assertEqual(response2.id, account_id)

    async def test_invalid_token_raises(self):
        bad_client = ApiClient('7')
        with self.assertRaises(GSMTasksError):
            await bad_client.accounts_list(q_page_size=1)

    async def test_list_param(self):
        ids = [
            'c3a0b9e4-df2b-44c4-b879-c0961dfc3620',
            '39f9a457-0d5a-40bd-9cb1-a6ff6207f584'
        ]
        tasks: list[Task] = await self.client.tasks_list(q_id__in=','.join(ids))

        pp([task.dict(exclude_none=True, exclude_unset=True) for task in tasks], stream=sys.stderr)

        self.assertEqual({UUID(hex=id_) for id_ in ids}, {task.id for task in tasks})

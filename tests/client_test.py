import logging
import os
import sys
from pprint import pp
from unittest import IsolatedAsyncioTestCase

from gsmtasks.client import ApiClient
from gsmtasks.components.schemas.account import Account
from gsmtasks.components.schemas.gsm_tasks_error import GSMTasksError

logging.basicConfig()
logging.getLogger('lapis_client_base').setLevel(logging.DEBUG)

client = ApiClient(os.environ['GSM_TASKS_TOKEN'])


class ClientTest(IsolatedAsyncioTestCase):
    async def test_single_param_query(self):
        response: list[Account] = await client.accounts_list(q_page_size=1)
        dicts = [task.dict(exclude_none=True, exclude_unset=True) for task in response]
        pp(dicts, stream=sys.stderr)
        self.assertEqual(len(response), 1)

        account_id = response[0].id
        response2 = await client.accounts_retrieve(p_id=account_id)
        self.assertEqual(response2.id, account_id)

    async def test_invalid_token_raises(self):
        bad_client = ApiClient('7')
        with self.assertRaises(GSMTasksError):
            await bad_client.accounts_list(q_page_size=1)

import logging
import os
import uuid

import pytest

from gsmtasks import ApiClient
from gsmtasks.components.schemas.GSMTasksError.schema import GSMTasksError
from gsmtasks.components.securitySchemes import api_key_tokenAuth

logging.basicConfig()
logging.getLogger('lapidary').setLevel(logging.INFO)


@pytest.fixture
def client_authenticated() -> ApiClient:
    client = ApiClient()
    client.lapidary_authenticate(api_key_tokenAuth(f"Token {os.environ['GSM_TASKS_TOKEN']}"))
    return client


@pytest.mark.asyncio
async def test_single_param_query(client_authenticated: ApiClient) -> None:
    response = (await client_authenticated.accounts_list(page_size_q=1)).body
    assert len(response) == 1
    account_id = response[0].id
    assert isinstance(account_id, uuid.UUID)

    response2 = (await client_authenticated.accounts_retrieve(id_p=account_id)).body
    assert response2.id == account_id


@pytest.mark.asyncio
@pytest.mark.skip(reason="global responses not supported")
async def test_invalid_token_raises(self):
    async with ApiClient() as client:
        client.lapidary_authenticate(api_key_tokenAuth('7'))

        with self.assertRaises(GSMTasksError):
            response = await client.accounts_list(page_size_q=1)
            print(response)


@pytest.mark.skip(reason="custom accept not supported")
@pytest.mark.asyncio
async def test_task_metadata(self):
    await self.client.tasks_retrieve(id_p='c3a0b9e4-df2b-44c4-b879-c0961dfc3620')
    # TODO custom metadata model


@pytest.mark.asyncio
async def test_simple_call(client_authenticated: ApiClient):
    await client_authenticated.accounts_list()

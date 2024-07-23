import logging
import os

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
    accounts, _ = await client_authenticated.accounts_list(page_size_q=1)
    assert len(accounts) == 1
    account_id = accounts[0].id

    account, _ = await client_authenticated.accounts_retrieve(id_p=account_id)
    assert account.id == account_id


@pytest.mark.asyncio
@pytest.mark.skip(reason="global responses not supported")
async def test_invalid_token_raises(client_authenticated: ApiClient):
    async with ApiClient() as client:
        client.lapidary_authenticate(api_key_tokenAuth('7'))

        with pytest.assertRaises(GSMTasksError):
            response = await client.accounts_list(page_size_q=1)
            print(response)


# @pytest.mark.skip(reason="custom accept not supported")
@pytest.mark.asyncio
async def test_task_metadata(client_authenticated: ApiClient):
    task, _ = await client_authenticated.tasks_retrieve(id_p='c3a0b9e4-df2b-44c4-b879-c0961dfc3620')
    print(type(task.metafields))
    print(task.metafields)
    # TODO custom metadata model


@pytest.mark.asyncio
async def test_simple_call(client_authenticated: ApiClient):
    await client_authenticated.accounts_list()


@pytest.mark.asyncio
async def test_task_id_in(client_authenticated: ApiClient):
    tasks, _ = await client_authenticated.tasks_list()
    assert len(tasks) == 100

    selected_task_ids = [task.id for task in tasks[:3]]
    tasks, _ = await client_authenticated.tasks_list(id__in_q=selected_task_ids)
    assert len(tasks) == 3
    assert [task.id for task in tasks[:3]] == selected_task_ids

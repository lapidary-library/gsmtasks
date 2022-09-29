Unofficial Python client for [GSMTasks API](https://api.gsmtasks.com/). 

This code is machine generated

## Licensing
As this code is machine generated, it's distributed as Public Domain.
If that's not acceptable to you, you may choose to use it under either CC0 or zero-clause BSD license.

Examples are programmed by a human and are distributed under either CC0 or zero-clause BSD licenses

## Usage
First, create a client:

```python
from gsmtasks.client import ApiClient

client = ApiClient(tokenAuth_authorization='YOUR API KEY')
```


Now call your endpoint and use your models:

```python
from gsmtasks.components.schemas.account import Account

response: list[Account] = await client.accounts_list(q_page_size=1)
```

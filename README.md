from lapidary.runtime.auth import HTTPfrom lapidary.runtime.auth import HTTPUnofficial Python client for [GSMTasks API](https://api.gsmtasks.com/). 

This code is machine generated using [Lapidary](https://github.com/python-lapidary/lapidary/).

## Licensing
As this code is machine generated, it's distributed as Public Domain.
If that's not acceptable to you, you may choose to use it under either CC0 or zero-clause BSD license.

Examples are programmed by a human and are distributed under either CC0 or zero-clause BSD licenses

## Usage

```python
from lapidary.runtime.auth import HTTP

from gsmtasks.client import ApiClient, Auth
from gsmtasks.components.schemas.account import Account

# First, create a client:

client = ApiClient(auth=Auth(tokenAuth=HTTP(token='YOUR API KEY')))


# Now call your endpoint and use your models:

response: list[Account] = await client.accounts_list(q_page_size=1)
```

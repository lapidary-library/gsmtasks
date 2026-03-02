Unofficial Python client for [GSMTasks API](https://api.gsmtasks.com/). 

This code is machine generated using [Lapidary](https://github.com/python-lapidary/lapidary/).

## Usage

```python
from importlib.metadata import version
from gsmtasks import ApiClient
from gsmtasks.components.securitySchemes import api_key_tokenAuth

# First, create a client:

client = ApiClient(
    headers = {
        'User-Agent': YOUR_CLIENT_NAME_VERSION,
    },
    timeout=30.,
)
client.lapidary_authenticate(api_key_tokenAuth('Token YOUR_TOKEN'))

# Now call your endpoint and use your models:

accounts, _ = await client.accounts_list()
```

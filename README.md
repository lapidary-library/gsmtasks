Unofficial Python client for [GSMTasks API](https://api.gsmtasks.com/). 

This code is machine generated using [Lapidary](https://github.com/python-lapidary/lapidary/).

## Usage

```python
from gsmtasks import ApiClient
from gsmtasks.components.securitySchemes import api_key_tokenAuth

# First, create a client:

client = ApiClient()
client.lapidary_authenticate(api_key_tokenAuth('Token ${YOUR API KEY}'))

# Now call your endpoint and use your models:

accounts, _ = await client.accounts_list()
```

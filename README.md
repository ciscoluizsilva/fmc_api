# Secure Firewall Managmenet Center API Framework 

- This is a WIP

## Objective - Have an Python API Framework to perform quick tasks

## Missing an API Endpoint ? Open an issue, and will address whenever possible.

## How to Install:
```
pip install git+https://github.com/ciscoluizsilva/fmc_api.git
```
## How to Update:
```
pip install -U https://github.com/ciscoluizsilva/fmc_api.git
```

## How to use:
### As an API Framkework:
```pyhton
from fmc_api import SecureFWMgmt

fmc_api = SecureFWMgmt(host=<FQDN_OR_UP>, username=<USERNAME>, password=<PASSWORD>)
# Write your own logic using the API Enpoints.
```

### Pre-Built Utility Scripts
```python

from fmc_api.utility.clean_unused_objects import clean

clean()
```

### List of Pre-Built Utilities:
1. fmc_api.utility.clean_unused_objects.clean()
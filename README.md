# Setup

1) Install any needed dependencies

```console
$ pip install -r requirements.txt
```

2) Create a file called `.robinhood_login`

Fill out the following and paste it into `.robinhood_login`

```
username: <your-username>
password: <your-password>
```

# Using

Before making any calls, make sure to run:

```
from utilities import robinhood_login
robinhood_login()
```

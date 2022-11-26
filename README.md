# AoiPy - Pycord made simple for learning
Latest Update: 11/26/22
#### Version: 0.5.0
### Using AoiPy
1 - `pip install AoiPy`

2 -

```python
from aoipy import *
from aoipy.BotUser import client
from aoipy.Users import Users
```

3 -  Example:

```python
from aoipy import *
from aoipy.BotUser import client
from aoipy.Users import Users
from aoipy.messages import messageable as ms

# ---------------Imports--------------------
act = client.activity("tv with friends", "watching")
bot = client.Bot(prefix="!", case_insensitive=False, intents=("all",), activity=act)


@bot.command()
async def cool(ctx):
    lol = await send(ctx, f"{Users.getMention(ctx.author)} is so cool!")
    await ms.deleteMessage(lol, 5)


run(bot, "*******<<TOKEN>>***********", f"Started on {bot.user}")
```

## New and still a work in progress
# AoiPy - Pycord made simple (By being very specific) for learning
Latest Update: 11/26/22
#### Version: 0.6.12
### Using AoiPy
1 - `pip install AoiPy`

2 -
```python
from aoipy.BotUser import client
from aoipy.Users import Users
```

3 -  Example:

```python
from aoipy.BotUser import client
from aoipy.messages import messageable as ms
# ---------------Imports--------------------
act = client.activity("tv", "watching")
bot = client.Bot(prefix="!", case_insensitive=False, intents=("all",), activity=act)


@bot.command()
async def cool(ctx):
    lol = await ms.sendChannelMessage(ctx, f"This command invoked in...")
    await ms.sendChannelMessage(ctx, ms.getMessageChannelName(lol))


client.run(bot, "*******<<TOKEN>>***********", f"Started on {bot.user}")
```

## New and still a work in progress
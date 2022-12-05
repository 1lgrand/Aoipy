# AoiPy - Discord.py made simple (By being very specific) for learning
Latest Update: 12/05/22
#### Version: 0.8.30
![AoiPY](https://github.com/LilbabxJJ-1/Aoipy/blob/master/aoipy/AOIpy%20(1).png)
### Using AoiPy
1 - `pip install AoiPy`

2 - Import Client and any other files
```python
from aoipy.BotUser import client
from aoipy.File import * 
```

3 -  Example:

```python
from aoipy.BotUser import client
from aoipy.Messages import *
from aoipy.Channels import *
# ---------------Imports--------------------
act = client.activity("tv", "watching")
bot = client.Bot(prefix="!", case_insensitive=False, intents=("all",), activity=act)


@bot.command()
async def where(ctx):
    await sendChannelMessage(ctx, f"This command invoked in...{getCurrentTextChannel(ctx)}")


client.run(bot, "*******<<TOKEN>>***********", f"Started on {bot.user}")
```

## New and still a work in progress

from aoipy.BotUser import client
from aoipy.Messages import messageable as ms
from aoipy.Users import member as mb
bot = client.Bot(prefix="!")


@bot.command()
async def ban(ctx):
    await mb.banMember(ctx.author, "For bein TOO cool!")
    await ms.sendChannelMessage(ctx, f"{ctx.author} has been banned!")

import aoipy
from aoipy.Client import *
from aoipy.Messages import *
from aoipy.Users import *
bot = client.Bot(prefix="!")


@bot.command()
async def ban(ctx, member: aoipy.Member):
    await banMember(member, "For bein TOO cool!")
    await sendChannelMessage(ctx, f"{member} has been banned!")

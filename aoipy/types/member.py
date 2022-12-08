import discord


class Member:
    async def banMember(self, member: discord.Member, reason: str = None):
        if reason is None:
            return await member.ban()
        else:
            return await member.ban(reason=reason)

    async def kickMember(self, member: discord.Member, reason: str = None):
        if reason is None:
            return await member.kick()
        else:
            return await member.kick(reason=reason)

    def getNick(self, member: discord.Member):
        return member.display_name

    def getRoles(self, member: discord.Member):
        return member.roles

    def getJoinDate(self, member: discord.Member):
        return member.joined_at

    def sendMessage(self, user: discord.User, message, embed: bool = False):
        if embed:
            user.send(embed=message)
        else:
            user.send(message)

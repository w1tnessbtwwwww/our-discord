from disnake.ext.commands import Cog, slash_command
from disnake import Interaction

class Ping(Cog):
    def __init__(self, bot):
        self.bot = bot 

    @slash_command(name="ping", description="Ping pong")
    async def ping(self, inter):
        await inter.send("Pong!")

def setup(bot):
    bot.add_cog(Ping(bot))
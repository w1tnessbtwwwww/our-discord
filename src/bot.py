from disnake.ext.commands import Bot as BaseBot, when_mentioned_or
from disnake import Activity, ActivityType, Intents



class Bot(BaseBot):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            test_guilds=[1123941641368109076],
            owner_ids=[315507881959096322, 315505638769819648],
            command_prefix=when_mentioned_or("!"),
            intents=Intents.all(),
            activity=Activity(
                type=ActivityType.watching,
                name="за твоей мамой",
                buttons=["Aboba"]
            ),
            
        )
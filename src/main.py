from bot import Bot
from config.config import config
import asyncio
import os
import datetime

bot: Bot = Bot()

@bot.event
async def on_ready():
    print(f"Start polling: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def load_extensions():
    for root, dirs, files in os.walk("src/cogs"):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root,file).replace('/', '.')[:-3]
                bot.load_extension(path.replace("src.", ""))
                print(f"loaded: {path}")

def main():
    load_extensions()
    bot.run(config.token)

if __name__ == "__main__":
    main()
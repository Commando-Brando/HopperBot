import os
import discord
import logging
from dotenv import load_dotenv
from discord.ext import commands


class TutorialBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Greetings
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} ({self.bot.user.id})')

    # Reconnect
    async def on_resume(self):
        print('Bot has reconnected')

    # Error Handlers
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(error)


# Gateway intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True

# Bot Prefix
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'),
                   description='A Simple Tutorial Bot', intents=intents)

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Loading data from .env files
load_dotenv()
token = os.getenv('TOKEN')

if __name__ == '__main__':
    # Load extension docs below
    # https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=load%20extension#discord.ext.commands.Bot.load_extension
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            bot.load_extension(f'commands.{filename[: -3]}')

    bot.add_cog(TutorialBot(bot))
    bot.run(token, reconnect=True)

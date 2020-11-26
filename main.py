from requests import get
import discord
from os import getenv

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        await client.change_presence(activity=discord.Game(name='!trump'))

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.lower() =='!trump':
            await message.channel.send(get('https://api.tronalddump.io/random/quote').json()['value'])

client = MyClient()
client.run(getenv('TRUMP_TOKEN'))
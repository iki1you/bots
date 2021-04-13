import discord
import asyncio
import requests

TOKEN = "ODMxNDg3NDc1Mzc2ODQ4OTM3.YHV9Dg.oXrQttBczVNDDc8HQqBmixAeCTs"


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'готов показать случайного котика (или пёсика!)\n'
                f'{guild.name}(id: {guild.id})')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "кот" in message.content.lower():
            a = requests.get('https://api.thecatapi.com/v1/images/search').json()
            a = a[0]['url']
            await message.channel.send(a)
        if "собака" or "пёс" in message.content.lower():
            a = requests.get('https://dog.ceo/api/breeds/image/random').json()
            a = a['message']
            await message.channel.send(a)


client = YLBotClient()
client.run(TOKEN)

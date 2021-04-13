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
                f'Пример ввода: "set_timer in 0 hours 1 minutes"\n'
                f'{guild.name}(id: {guild.id})')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "set_timer in" in message.content.lower():
            hours = 0
            minutes = 0
            seconds = 0
            a = list(message.content.lower().split())
            if "hours" in message.content.lower():
                hours = a[a.index("hours") - 1]
            if "minutes" in message.content.lower():
                minutes = a[a.index("minutes") - 1]
            if "seconds" in message.content.lower():
                seconds = a[a.index("seconds") - 1]
            await message.channel.send(f"The timer should start in {hours} hours "
                                       f"{minutes} minutes {seconds} seconds.")
            await asyncio.sleep(int(hours) * 60 * 60 + int(minutes) * 60 + int(seconds))
            await message.channel.send(":alarm_clock:Time X has come!")


client = YLBotClient()
client.run(TOKEN)
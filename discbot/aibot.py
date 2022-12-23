import os
import discord
from dotenv import load_dotenv
from apibot import Question




load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1055654694531383399
intents = discord.Intents(messages=True, guilds=True)
client = discord.Client(intents=intents)




class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == client.user:
            return
        
        if message.channel.id != CHANNEL_ID:
            return
        
        #ask question to open ai api
        q = Question(message.content)
        answer = q.get_answer()
        await message.channel.send(f'```{answer}```')
        print(f'Message from {message.author}: {message.content}')
        

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)



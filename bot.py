import discord
import responses

async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE4NzkzNzQ3NjA3NDAyOTA5Ng.GTR4Lg.thiJqaBux9Q6pxts6bn5fxNOerNXByEOJm87pQ'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("cliche")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        user_msg = str(message.content)

        await send_message(message, user_msg)

    client.run(TOKEN)
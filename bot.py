import discord
import responses

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE4NzkzNzQ3NjA3NDAyOTA5Ng.GTR4Lg.thiJqaBux9Q6pxts6bn5fxNOerNXByEOJm87pQ'
    intent = discord.Intents.default()
    intent.message_content = True
    client = discord.Client(intents=intent)

    @client.event
    async def on_ready():
        print("cliche")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        user_message = str(message.content)
        args = user_message.split()
        if(args[0].lower() != "cliche" and args[0].lower() != "plot"):
            return
        if(len(args) > 2 or len(args) ==0):
            return
        await send_message(message, user_message)

    client.run(TOKEN)
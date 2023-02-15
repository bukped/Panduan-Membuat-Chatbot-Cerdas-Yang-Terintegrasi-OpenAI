import openai
import discord
import openai_secret_manager

# Mengambil API key dari OpenAI
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secrets("openai")

# Importing the OpenAI library


# Setting the API key
openai.api_key = secrets["api_key"]

# Inisialisasi client bot dengan token
client = discord.Client()

# Event handler untuk pesan yang diterima


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # Logika untuk menangani pesan yang diterima
    prompt = (f"{message.content}")

    # Menggunakan fungsi generate untuk menghasilkan teks
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Menanggapi pesan yang diterima
    await message.channel.send(response["choices"][0]["text"])

# Menjalankan client bot
client.run("TOKEN_BOT_DISCORD")

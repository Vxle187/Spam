import discord
from discord import app_commands
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot ist eingeloggt als {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Slash-Commands synchronisiert: {len(synced)}")
    except Exception as e:
        print(f"Fehler beim Synchronisieren: {e}")

@bot.tree.command(name="spam", description="Nerve jemanden mit 100 Nachrichten")
@app_commands.describe(
    message="Die Nachricht, z. B. 'Wach auf!'",
    user="Wen willst du ärgern?"
)
async def spam(interaction: discord.Interaction, message: str, user: discord.User):
    await interaction.response.send_message(f"Starte Spam gegen {user.mention} ...", ephemeral=True)

    for i in range(100):
        content = f"{user.mention} {message} ({i+1}/100)"
        await interaction.channel.send(content)
        await asyncio.sleep(0.7)  # Verzögerung, um Rate-Limit zu vermeiden

bot.run("DEIN_BOT_TOKEN")

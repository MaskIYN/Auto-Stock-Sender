import os
import sys
import asyncio
from colorama import Fore
import time
import discord
import time
from datetime import datetime
from discord.ext import commands

def sprint(content: str, status: str = "c") -> None:
    current_time = datetime.now().strftime("%H:%M:%S")
    sys.stdout.write(f"[>] {current_time} : {content}{Fore.RESET}\n")

os.system("pip install discord.py==1.7.3")
os.system("clear")

client = discord.Client(intents=discord.Intents.default())

token = "MTA3NDkwOTk0Murmom.69" #ur token here

send = commands.Bot(command_prefix=">", self_bot=True)

Message = ("""msg here""") #Message

@send.event 
async def on_ready():
  print(f"Connected To: {send.user}")
  guild = send.get_guild(1101581015601926236) #server id
  while True:
    await asyncio.sleep(10) #Time
    for channel in guild.channels:
      if channel.name == "・stocks﹒・": #channel name
        await channel.send(Message)
        sprint(f"""{Fore.CYAN}[SENT] {Fore.LIGHTWHITE_EX}Successfully Sent!""")

send.run(token, bot=False)

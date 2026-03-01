import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

# Get credentials from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
string_session = os.getenv("STRING_SESSION")  # this will be set on Railway

# Create the client
client = TelegramClient(StringSession(string_session), api_id, api_hash)

# Example: forward messages from source_channel to target_channel
source_channel = "Astrology_Cou"
target_channel = "astrologynumerologyvastu"    # replace with your channel

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    await event.message.forward_to(target_channel)

async def main():
    print("Bot is running...")
    await client.run_until_disconnected()

asyncio.run(main())

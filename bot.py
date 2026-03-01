import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
string_session = os.getenv("STRING_SESSION")

client = TelegramClient(StringSession(string_session), api_id, api_hash)

source_channel = "Astrology_Cou"  # without @
target_channel = "astrologynumerologyvastu"   # with @

async def main():
    print("Connecting to Telegram...")
    await client.start()  # ensures client is connected
    print("Bot is running and connected!")

    @client.on(events.NewMessage(chats=source_channel))
    async def handler(event):
        await event.message.forward_to(target_channel)

    await client.run_until_disconnected()  # keeps bot alive

asyncio.run(main())

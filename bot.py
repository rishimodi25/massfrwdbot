import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
string_session = os.getenv("STRING_SESSION")

client = TelegramClient(StringSession(string_session), api_id, api_hash)

source_channel = "Astrology_Cou"
target_channel = "astrologynumerologyvastu"

async def main():
    await client.start()
    print("Connected!")

    source = await client.get_entity(source_channel)
    target = await client.get_entity(target_channel)

    print("Channels OK")

    # Only test 5 messages first
    async for message in client.iter_messages(source, limit=5):
        print("Forwarding:", message.id)
        await message.forward_to(target)

    print("Now listening...")

    @client.on(events.NewMessage(chats=source))
    async def handler(event):
        print("New message detected")
        await event.message.forward_to(target)

    await client.run_until_disconnected()

asyncio.run(main())

import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
string_session = os.getenv("STRING_SESSION")

client = TelegramClient(StringSession(string_session), api_id, api_hash)

source_channel = "Astrology_Cou"  # without @ 
target_channel = "astrologynumerologyvastu"   # with @

async def main():
    await client.start()
    print("Bot connected!")

    # --- Forward all old messages ---
    async for message in client.iter_messages(source_channel, reverse=True):
        try:
            await message.forward_to(target_channel)
        except Exception as e:
            print(f"Failed to forward message {message.id}: {e}")

    print("All old messages forwarded!")

    # --- Listen for new messages ---
    @client.on(events.NewMessage(chats=source_channel))
    async def handler(event):
        await event.message.forward_to(target_channel)

    await client.run_until_disconnected()
    async for message in client.iter_messages(source_channel, limit=100, reverse=True):

asyncio.run(main())

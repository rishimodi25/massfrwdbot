import os
import asyncio
from telethon import TelegramClient, events

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

source_channel = "Astrology_Cou"   # without @
target_channel = "astrologynumerologyvastu"     # without @

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    text = event.message.text
    if not text:
        return

    # Edit words
    text = text.replace("@Slayber007", "@vishnuisbck")

    await client.send_message(target_channel, text)

async def main():
    await client.start()
    print("Userbot is running...")
    await client.run_until_disconnected()

asyncio.run(main())

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

# 🔥 Words to replace
REPLACE_MAP = {
    "@Slayber007": "@vishnuisbck",
}

def replace_words(text):
    if not text:
        return text
    
    for old, new in REPLACE_MAP.items():
        text = text.replace(old, new)
    
    return text


async def main():
    await client.start()
    print("Connected!")

    source = await client.get_entity(source_channel)
    target = await client.get_entity(target_channel)

    print("Channels OK")

    print("Copying last 100 messages...")

    async for message in client.iter_messages(source, limit=100):
        try:
            print("Processing:", message.id)

            new_text = replace_words(message.text)

            if message.text:
                await client.send_message(target, new_text)

            elif message.media:
                await client.send_file(
                    target,
                    message.media,
                    caption=new_text
                )

            await asyncio.sleep(1)

        except Exception as e:
            print("Skipped:", message.id, e)

    print("Listening for new messages...")

    @client.on(events.NewMessage(chats=source))
    async def handler(event):
        try:
            msg = event.message
            new_text = replace_words(msg.text)

            if msg.text:
                await client.send_message(target, new_text)

            elif msg.media:
                await client.send_file(
                    target,
                    msg.media,
                    caption=new_text
                )

        except Exception as e:
            print("New msg error:", e)

    await client.run_until_disconnected()

asyncio.run(main())

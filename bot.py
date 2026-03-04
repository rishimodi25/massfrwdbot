import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
string_session = os.getenv("STRING_SESSION")

client = TelegramClient(StringSession(string_session), api_id, api_hash)

# 🔴 PRIVATE CHANNEL ID (must start with -100)
source_channel = 1430487486   # <-- PUT REAL ID HERE
target_channel = "astrologynumerologyvastu"

# Words to replace
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
    print("✅ Userbot connected!")

    try:
        source = await client.get_entity(source_channel)
        target = await client.get_entity(target_channel)
        print("✅ Channels found")
    except Exception as e:
        print("❌ Channel error:", e)
        return

    print("🔁 Forwarding last 100 old messages safely...")

    async for message in client.iter_messages(source, limit=100, reverse=True):
        try:
            if message.text:
                await client.send_message(
                    target,
                    replace_words(message.text)
                )
            elif message.media:
                await client.send_file(
                    target,
                    message.media,
                    caption=replace_words(message.text)
                )

            await asyncio.sleep(1)  # Safe delay

        except Exception as e:
            print("Old msg error:", e)

    print("✅ Old messages done")
    print("👂 Listening for new messages...")

    @client.on(events.NewMessage(chats=source))
    async def handler(event):
        try:
            msg = event.message

            if msg.text:
                await client.send_message(
                    target,
                    replace_words(msg.text)
                )
            elif msg.media:
                await client.send_file(
                    target,
                    msg.media,
                    caption=replace_words(msg.text)
                )

        except Exception as e:
            print("New msg error:", e)

    await client.run_until_disconnected()


asyncio.run(main())

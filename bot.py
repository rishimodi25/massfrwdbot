import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
string_session = os.getenv("STRING_SESSION")

client = TelegramClient(StringSession(string_session), api_id, api_hash)

source_channel = "Astrology_Cou"
target_channel = "@astrologynumerologyvastu"

async def main():
    await client.start()
    print("Connected!")

    source = await client.get_entity(source_channel)
    target = await client.get_entity(target_channel)

    print("Channels OK")

    async for message in client.iter_messages(source, limit=100):
        try:
            print("Copying:", message.id)

            if message.text:
                await client.send_message(target, message.text)

            elif message.media:
                await client.send_file(
                    target,
                    message.media,
                    caption=message.text
                )

            await asyncio.sleep(1)

        except Exception as e:
            print("Skipped message:", message.id, e)

    print("Now listening...")

    @client.on(events.NewMessage(chats=source))
    async def handler(event):
        msg = event.message

        if msg.text:
            await client.send_message(target, msg.text)

        elif msg.media:
            await client.send_file(
                target,
                msg.media,
                caption=msg.text
            )

    await client.run_until_disconnected()

asyncio.run(main())

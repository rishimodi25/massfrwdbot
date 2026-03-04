from telethon import TelegramClient
from telethon.sessions import StringSession
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
string_session = os.getenv("STRING_SESSION")

client = TelegramClient(StringSession(string_session), api_id, api_hash)

async def main():
    await client.start()
    
    async for dialog in client.iter_dialogs():
        print(dialog.name, "=>", dialog.id)

with client:
    client.loop.run_until_complete(main())

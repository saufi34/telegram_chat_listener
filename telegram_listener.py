
from telethon import TelegramClient, events

# Replace with your API credentials
api_id = ''  # Your API ID from my.telegram.org
api_hash = ''  # Your API Hash from my.telegram.org
phone_number = ''  # Your personal Telegram phone number

# Create the client and connect
client = TelegramClient('test_session', api_id, api_hash)

# This function will just print any message received from the specified channel
@client.on(events.NewMessage(chats=1002000236837))  # Replace with your channel username or ID
async def message_handler(event):
    message = event.message.message
    print(f"Message received: {message}")  # Print the message to the console

# Start the client
async def main():
    await client.start(phone=phone_number)  # Logs in using your phone number
    print("Listening for messages...")
    await client.run_until_disconnected()  # Keeps the client running and listening for messages

with client:
    client.loop.run_until_complete(main())



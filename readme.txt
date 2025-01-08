# Telegram Channel Message Listener

## Overview
This script uses the **Telethon** library to create a Telegram client that listens for incoming messages from a specified Telegram channel and logs the content to the console. It is useful for monitoring channel activity programmatically.

## Prerequisites

1. **Python Installed**: Ensure you have Python 3.7 or higher installed.
2. **Telethon Library**: Install the Telethon library by running:
   ```bash
   pip install telethon
   ```
3. **Telegram API Credentials**: Obtain your API ID and API Hash from [my.telegram.org](https://my.telegram.org/).
4. **Telegram Channel ID**: Know the unique ID or username of the Telegram channel you want to monitor.

## Configuration
Replace the placeholder values in the script with your own:
- `api_id`: Your API ID from Telegram.
- `api_hash`: Your API Hash from Telegram.
- `phone_number`: Your personal Telegram phone number.
- `chats`: The channel ID or username you want to monitor.

Example:
```python
api_id = '123456'
api_hash = 'abcdef1234567890'
phone_number = '+123456789'

# Replace with your channel ID or username
@client.on(events.NewMessage(chats=123456789))
```

## Features
- Connects to your Telegram account using Telethon.
- Monitors messages from a specific Telegram channel.
- Logs the content of incoming messages to the console.

## How to Run
1. Save the script to a file (e.g., `telegram_channel_listener.py`).
2. Run the script using Python:
   ```bash
   python telegram_channel_listener.py
   ```
3. Upon running, the script will:
   - Authenticate your Telegram account.
   - Start listening for messages from the specified channel.
   - Print each received message to the console.

## Example Output
When a message is received, the script logs details like this:
```
Message received: Welcome to the channel!
```


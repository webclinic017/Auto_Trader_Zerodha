# TelegramLink.py
import asyncio
from telegram import Bot
from Auto_Trader.my_secrets import TG_TOKEN, CHANNEL

# Initialize the bot globally
bot = Bot(token=TG_TOKEN)

async def send_to_channel(message_queue):
    """Asynchronously sends messages from the queue to the Telegram channel."""
    while True:
        message = message_queue.get()  # Wait for the next message from the queue
        print(message)
        if message == "STOP":
            break  # Exit if STOP is received
        try:
            await bot.send_message(chat_id=CHANNEL, text=message)
            print(f"Message sent: {message}")
        except Exception as e:
            print(f"Error sending message: {e}")

def telegram_main(message_queue):
    """Main function to handle the Telegram message sending process."""
    asyncio.run(send_to_channel(message_queue))
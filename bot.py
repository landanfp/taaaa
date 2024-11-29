
from pyrogram import Client, filters
import time

API_ID = "3335796" 
API_HASH = "138b992a0e672e8346d8439c3f42ea78"
BOT_TOKEN = ""

# Initialize the bot with your API credentials
app = Client("my_bot", BOT_TOKEN=BOT_TOKEN, API_ID=API_ID, API_HASH=API_HASH)

@app.on_message(filters.command("create"))
async def create_command(client, message):
    # Simulate typing indicator
    await message.reply("Please wait while I create something...")

    # Start the typing action (indicating the bot is processing)
    async with message.chat.typing():
        # Simulate some time-consuming task, e.g., creating something
        time.sleep(3)  # You can replace this with any long-running task

    # After the task is done, send a response
    await message.reply("Creation complete! 🎉")

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply("Welcome! Use /create to trigger the creation process.")

if __name__ == "__main__":
    app.run()

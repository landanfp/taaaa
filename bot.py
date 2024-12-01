from pyrogram import Client
import time

# Replace with your actual API ID and API Hash
api_id = '3335796'  # Your API ID
api_hash = '138b992a0e672e8346d8439c3f42ea78'  # Your API Hash
bot_token = ''
# Create a Client instance (use your phone number or bot token)
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# The function that runs the bot
@app.on_message()
def handle_message(client, message):
    # If you want to reply to the message
    if message.text:
        # Send typing status to the user
        message.chat.send_action("typing")

        # Wait for a second to simulate typing
        time.sleep(2)

        # Reply to the message
        message.reply("Hello! This is an automated response.")

# Run the client
app.run()

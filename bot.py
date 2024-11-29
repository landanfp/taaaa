from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Replace with your bot's API token
API_TOKEN = "7136875110:AAF3hNDcTC4X2e9GQ7EePvOST7aTCPh1pGg"
API_HASH = "138B992A0E672E8346D8439C3F42EA78"
API_ID = 3335796
app = Client("my_bot", bot_token=API_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Handler for /start command
@app.on_message(filters.command("start"))
async def start(client, message):
    # Create an InlineKeyboardMarkup object with a button
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Click Me", callback_data="button_clicked")]
        ]
    )
    
    # Send a message with an inline keyboard
    await message.reply(
        "Welcome! Click the button below:",
        reply_markup=keyboard
    )

# Handler for the button click (callback query)
@app.on_callback_query(filters.regex("button_clicked"))
async def button_clicked(client, callback_query):
    await callback_query.answer("You clicked the button!")

# Start the bot
app.run()

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Replace with your bot's API token
BOT_TOKEN = "7136875110:AAF3hNDcTC4X2e9GQ7EePvOST7aTCPh1pGg"
API_HASH = "138B992A0E672E8346D8439C3F42EA78"
API_ID = 3335796
app = Client("my_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Handler for /start command
@bot.on.message(filters.command('start') & filters.private )
def command(bot, message):
bot.send.message(message.chat.id, "Hello Baby")
print ("i am online")

@bot.on.message(filters.command('help')  )
def command1(bot, message):
message.reply_text("Hello help")
print ("i am helping")

@bot.on_message(filters.text)
def echobot(client, message): message.reply_text(message.text)
print ("i am testing")


# Start the bot
app.run()

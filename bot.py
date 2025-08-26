import os
import telebot

# Get token from Railway environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! 🚀 Your Railway bot is running successfully.")

print("Bot is running...")
bot.infinity_polling()

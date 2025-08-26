import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Get token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

filters_dict = {}  # Dictionary to store permanent filters

# Start command
def start(update, context):
    update.message.reply_text("Hello! I am your filter bot. Use /addfilter <word> <reply>")

# Add filter
def add_filter(update, context):
    if len(context.args) < 2:
        update.message.reply_text("Usage: /addfilter <word> <reply>")
        return
    word = context.args[0].lower()
    reply = " ".join(context.args[1:])
    filters_dict[word] = reply
    update.message.reply_text(f"✅ Filter added for '{word}'")

# Delete filter
def del_filter(update, context):
    if len(context.args) < 1:
        update.message.reply_text("Usage: /delfilter <word>")
        return
    word = context.args[0].lower()
    if word in filters_dict:
        del filters_dict[word]
        update.message.reply_text(f"🗑️ Filter removed for '{word}'")
    else:
        update.message.reply_text("❌ No such filter found")

# List filters
def list_filters(update, context):
    if not filters_dict:
        update.message.reply_text("No filters set yet.")
        return
    text = "📌 Current Filters:\n" + "\n".join([f"- {k}: {v}" for k,v in filters_dict.items()])
    update.message.reply_text(text)

# Respond to filters
def check_filters(update, context):
    msg = update.message.text.lower()
    for word, reply in filters_dict.items():
        if word in msg:
            update.message.reply_text(reply)
            break

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("addfilter", add_filter))
    dp.add_handler(CommandHandler("delfilter", del_filter))
    dp.add_handler(CommandHandler("listfilters", list_filters))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, check_filters))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

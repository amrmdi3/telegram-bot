from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# جایگزین کن با توکن واقعی خودت 👇
API_TOKEN = '7794824509:AAENhfGWfGfgVWDTDGyrOH7mATRIZtEfvik'

# دستور /start


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من اولین ربات تو هستم 😊")

# تکرار پیام‌ها


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

# اجرا
if __name__ == '__main__':
    app = ApplicationBuilder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("ربات روشن شد ✅")
    app.run_polling()

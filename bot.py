import logging

from telegram import Update, constants
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    CallbackContext,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm not angry, I'm just disappointed.",
    )

async def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = (
        ApplicationBuilder()
        .token("7283089275:AAFiNerCfDdUZY4pT-noATezv5CoXNqppRg")
        .connect_timeout(30)
        .pool_timeout(15)
        .build()
    )
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    # on non-command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    # Run the bot until you press Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()

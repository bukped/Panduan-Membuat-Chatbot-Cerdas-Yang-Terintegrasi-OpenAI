# import telegram
from telegram.ext import Updater, CommandHandler


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hi, I'm a Telegram bot.")


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I can do a lot of things!")


def hi(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hi Juga!")


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)


def main():
    # Create Telegram Bot
    token = " YOUR_API_TOKEN"
    bot = telegram.Bot(token=token)
    updater = Updater(token=token, use_context=True)

    # Add handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("help", help))
    updater.dispatcher.add_handler(CommandHandler("echo", echo))
    updater.dispatcher.add_handler(CommandHandler("hi", hi))

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

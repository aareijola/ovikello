import os
from dotenv import load_dotenv
import telebot

load_dotenv()
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
TELEGRAM_GRP_ID = os.getenv("TELEGRAM_GRP_ID")
bot = telebot.TeleBot(TELEGRAM_API_KEY)


def main():
    print("Hello")
    bot.send_message(TELEGRAM_GRP_ID, "SAATANA")


if __name__ == "__main__":
    main()

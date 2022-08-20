import telebot
import os
from loguru import logger

#print(os.environ["TELEGRAMBOT_TOKEN"])
class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ["TELEGRAMBOT_TOKEN"], parse_mode=None)
        self.send_welcome(message)=self.bot.message_handler(commands=['start', 'help'])

    def send_welcome(message):
	    bot.reply_to(message, "Hey!")


    def run(self):
        logger.info("Running bot ...")
        self.bot.polling()


if __name__ == '__main__':
    bot = Bot()




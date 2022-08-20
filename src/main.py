import telebot
import os
from loguru import logger

#print(os.environ["TELEGRAMBOT_TOKEN"])
class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ["TELEGRAMBOT_TOKEN"], parse_mode=None)
        self.respond_welcome=self.bot.message_handler(commands=['start', 'help'])(self.respond_welcome)
        self.respond_text=self.bot.message_handler(func=lambda message: True)(self.respond_text)


    def respond_welcome(self, message):
        self.set(message)
	    self.bot.reply_to(message, f"Hey {self.name}!")


    def respond_text(self, message):
        self.set(message)
	    self.bot.send_message(message.chat.id, f'Hey {self.name}!')


    def set(self, message):
        self.name = message.chat.first_name
        if message.chat.last_name:
            self.name = f"{self.name} {self.last_name}"
        self.chat_id = message.chat.id
        logger.info(f'chat id: {self.chat_id}')


    def run(self):
        logger.info("Running bot ...")
        self.bot.polling()



if __name__ == '__main__':
    bot = Bot()
    bot.run()







import os
import telebot


TOKEN = os.environ['API_TOKEN']
      bot = telebot.TeleBot(TOKEN)
          @bot.message_handler(commands=['start'])
          def start(message):
              bot.reply_to(message, "Hello, did someone call for help?")

bot.polling
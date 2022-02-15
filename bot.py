

import os
import telebot
TOKEN = '5120823518:AAFYN0Y_9YTislvL0pklBfxxm9PYjOXj8dk'
      bot = telebot.TeleBot(TOKEN)
          @bot.message_handler(commands=['start', 'help'])
          def command_help(message):
              bot.reply_to(message, "Hello, did someone call for help?")


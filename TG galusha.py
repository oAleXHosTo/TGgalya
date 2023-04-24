import telebot
from telebot import types
token='5975097585:AAGwsnuw7cbWKFSn33ptPeasHSLDEsd51ps'
bot = telebot.TeleBot('5975097585:AAGwsnuw7cbWKFSn33ptPeasHSLDEsd51ps')
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_poling()

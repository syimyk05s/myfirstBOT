import telebot
from telebot import types

bot = telebot.TeleBot('6713619010:AAHqpYdPWckRYESJACHF0tTUSeaHTmJpuoA')


@bot.message_handler(commands=['start'])
def start(message):
    mrsfk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    asd1 = types.KeyboardButton('')
    asd2 = types.KeyboardButton('')
    mrsfk.add(asd1, asd2)
    bot.send_message(message.chat.id, text="Hello {0.first_name}! I am bot".format(
        message.from_user), reply_markup=markup)
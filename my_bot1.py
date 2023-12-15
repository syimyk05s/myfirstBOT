import telebot
from telebot import types

bot = telebot.TeleBot('6713619010:AAHqpYdPWckRYESJACHF0tTUSeaHTmJpuoA')

@bot.message_handler(commands=['Hi'])
def start(message):
    mess = f'Hi <b><u>{message.from_user.first_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# @bot.message_handler()
# def user(message):
#     if message.text == 'Alina':
#         bot.send_message(message.chat.id, 'Hi Alinka')
#     elif message.text == 'Begim':
#         bot.send_message(message.chat.id, 'HI Begimka')
#     elif message.text == 'Pic':
#         photo = open('Снимок экрана 2023-11-28 в 16.19.32.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "i no understand")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("Задать вопрос❓")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я помошник Менторов по Python".format(
                         message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text=' за помошью ко мне правильное решение!')

    elif (message.text == "Задать вопрос❓"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Что я могу?')
        btn2 = types.KeyboardButton('Кто мой создатель?')
        btn3 = types.KeyboardButton('Вернутся в главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text='Выбирай вопрос!', reply_markup=markup)

    elif (message.text == 'Кто мой создатель?'):
        bot.send_message(message.chat.id, text='Мой создатель BOOTCAMP_21')

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Я могу показать 3х месячную программу по изучению (PYTHON)")
        murkup_inline = types.InlineKeyboardMarkup()
        item_yes = types.InlineKeyboardButton(text='Показать', callback_data='yes')
        item_no = types.InlineKeyboardButton(text='Отменить', callback_data='no')
        murkup_inline.row(item_yes, item_no)
        bot.send_message(message.chat.id, text="Показать вам список курса?", reply_markup=murkup_inline)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.data == 'yes':
                bot.send_message(call.message.chat.id, 'Выбирай из ряда свой месяц')
                markup_inline = types.InlineKeyboardMarkup()
                bot.send_message(call.message.chat.id, 'Список курса:', reply_markup=markup_inline)
            elif call.data == 'no':
                bot.send_message(call.message.chat.id, 'Хорошо, не буду показывать список курса.')


    elif (message.text == "Вернутся в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("Задать вопрос❓")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не отвечаю прости..\n Мой создатель будет ругать)")



@bot.message_handler(commands=['site'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Квакртира тууралуу маалыматтар!', url='https://lalafo.kg'))
    bot.send_message(message.chat.id, 'Бул жакты бас', reply_markup=markup)

bot.polling(none_stop=True)


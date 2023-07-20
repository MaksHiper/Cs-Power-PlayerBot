import telebot
from telebot import types
from config import bot
from background import keep_alive
import pip
pip.main(['install', 'pytelegrambotapi'])



allowed_user_ids = [1330775721]
bot = bot
users = set()

@bot.message_handler(commands=['get_chat_id'])
def handle_get_chat_id(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f'Ваш id: {chat_id}')

@bot.message_handler(commands=['send_summary'])
def send_summary(message):
  if message.from_user.id in allowed_user_ids:
    with open('users.txt', 'r') as file:
        users = file.read().splitlines()
    for user in users:
        bot.send_message(user, "Бот обновился!")

@bot.message_handler(commands=['contact_admin'])
def contact_admin(message):
    chat_id = message.chat.id
    if chat_id != 1330775721:
        bot.send_message(1330775721, f"User ID: {chat_id}\nMessage: {message.text}")
        bot.reply_to(message, "Ваше сообщение отправлено администратору.")
    else:
        bot.reply_to(message, "Вы администратор")




@bot.message_handler(commands=['start'])
def start(message):
    users.add((message.chat.id, message.chat.username))
    with open('users.txt', 'w') as file:
        for user in users:
            file.write(f"{user[0]} {user[1]}\n")
    bot.reply_to(message, 'Мы рады что вы выбрали нас!💚')
 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton('Меню')
    item2 = types.KeyboardButton('Инжектор')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id, 'Bыбери чит и получи ссылку на скачивание.\nЕсли понравится можете оставить отзыв😁https://t.me/CheatsCs_bot_otzivi\nКоманды:\n/get_chat_id') 

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Читы')
            item2 = types.KeyboardButton('Кфг')
            item3 = types.KeyboardButton('Cs2020')           
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2,item3, back)

            bot.send_message(message.chat.id, 'меню', reply_markup=markup)

        elif message.text == 'Читы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Fatality')
            item2 = types.KeyboardButton('Airflow')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Читы', reply_markup=markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Меню')
            item2 = types.KeyboardButton('Инжектор')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)

        elif message.text == 'Кфг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('OtherCfg')
            item2 = types.KeyboardButton('RazeCfg')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Кфг', reply_markup=markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Меню')
            item2 = types.KeyboardButton('Инжектор')

            markup.add(item1, item2)
        elif message.text == 'Cs2020':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('CsGo2020')
            item2 = types.KeyboardButton('OtcV2')
            item3 = types.KeyboardButton('OtcV3')
            item4 = types.KeyboardButton('PandoraV3')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2,item3,item4, back)

            bot.send_message(message.chat.id, 'Cs2020', reply_markup=markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Меню')
            item2 = types.KeyboardButton('Инжектор')

            markup.add(item1, item2)
  
        if message.text == 'Fatality':
         bot.send_message(message.chat.id,'https://drive.google.com/drive/folders/1P5QFjRikeNkbdzq1P4CMh1j7MjwetYRy?usp=drive_link')
        elif message.text == 'Airflow':
          bot.send_message(message.chat.id,'https://drive.google.com/drive/folders/1bvwzFbzVUjTlo86nW002EmYW_iOTGSXW?usp=drive_link')
        elif message.text == 'Инжектор':
          bot.send_message(message.chat.id, 'https://github.com/master131/ExtremeInjector/releases')
        elif message.text == 'OtherCfg':
          bot.send_message(message.chat.id, 'https://drive.google.com/drive/folders/1-q4Cwv08pQNoCxYpTBVXCIW0OhEg2G4j?usp=sharing')
        elif message.text == 'RazeCfg':
          bot.send_message(message.chat.id, 'https://drive.google.com/drive/folders/1Q9EH0nvhAfTWuOauJhzRgGIz669VFAvu?usp=drive_link')

        elif message.text == 'OtcV3':
         bot.send_message(message.chat.id, 'https://github.com/de0ver/Cheats-2020/blob/main/1lugi3g.dll')

        elif message.text == 'OtcV2':
         bot.send_message(message.chat.id, 'https://github.com/de0ver/Cheats-2020/blob/main/OTC_1.dll')
        elif message.text == 'CsGo2020':
         bot.send_message(message.chat.id, 'https://disk.yandex.ru/d/0YZ_GK1ZQRRdNg')
        elif message.text == 'PandoraV3':
         bot.send_message(message.chat.id, 'https://github.com/de0ver/Cheats-2020/blob/main/pandora_v3.dll')
        
keep_alive()
bot.polling(none_stop=True)



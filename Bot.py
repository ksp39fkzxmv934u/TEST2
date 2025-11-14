import telebot
from telebot import types

WebApp = types.WebAppInfo(url="???")

BotToken = "???"
bot = telebot.TeleBot(BotToken, parse_mode=None)

@bot.message_handler(commands=["start"])
def message1(msg):
    m = types.InlineKeyboardMarkup()
    m.add(types.InlineKeyboardButton("Начать", web_app=WebApp))
    bot.send_message(msg.chat.id, "@" + msg.from_user.username + "\nНажмите на кнопку чтобы войти в игру", reply_markup=m)

bot.infinity_polling()

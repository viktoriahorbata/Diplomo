import telebot
from telebot import types

bot = telebot.TeleBot('7451854122:AAH3FpAxw9hCYq2cjNAqLHjAZaYDyNhB7sw')

@bot.message_handler(commands=['start'])
def question(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    iron = types.InlineKeyboardButton('Мені потрібна допомога', callback_data='answer_iron')
    cotton = types.InlineKeyboardButton('Хочу допомогти', callback_data='answer_cotton')
    same = types.InlineKeyboardButton('Про Вільні душі', callback_data='answer_same')
    no_answer = types.InlineKeyboardButton('Які проекти сайту у нас є?', callback_data='no_answer')
    markup.add(iron, cotton, same, no_answer)
    bot.send_message(message.chat.id, 'Що вам потрібно?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def answer(callback):
    if callback.message:
        if callback.data == 'answer_same':
            bot.send_message(callback.message.chat.id, 'Вільні душі - це платформа онлайн-благодійності, ефективний та сучасний інструмент для залучення коштів на благодійні та соціальні проєкти будь-якого спрямування. Платформа "Вільні душі" є потужною комунікаційною платформою для благодійного сектору, зручним онлайн-сервісом, який щодня дозволяє зустрітися тисячам людей. Тим, хто потребує допомоги, і тим - хто може допомогти. Ми не лише залучаємо та скеровуємо гроші туди, де вони найгостріше необхідні, ми відкриваємо доступ некомерційним організаціям до ідей та інформації, а бізнесу — до найпрозоріших організацій та можливості отримати повну фінансову звітність.')
        elif callback.data == 'answer_iron':
            bot.send_message(callback.message.chat.id, 'Напишіть, що саме вам потрібно та свої прізвище імя та номер телефону. Наші менеджери оброблять ваш запит, та звяжуться з вами.')
        elif callback.data == 'answer_cotton':
            bot.send_message(callback.message.chat.id, 'Ви можете допомогти військовим, своїм донатом! Рексвізити для допомоги:\n - номер карти приватбанку: 5457 0822 9346 4181;\n - номер карти ощадбанку: 5375 4112 1976 6578;\n - номер карти монобанку: 5375 4141 2501 2863;\n - посилання на банку збору у монобанку: https://send.monobank.ua/jar/6R8xhhZKqf.')
        else:
            bot.send_message(callback.message.chat.id, 'Ось посилання на проекти: https://utkaaa.github.io/Free-Souls/index.html. На сайті ви знайдете детальну інформацію.')

bot.polling()

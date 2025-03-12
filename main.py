import telebot
from telebot import types

#Токен для того, чтобы скрипт мог отправлять сообщения в телегу.
bot = telebot.TeleBot('7490490371:AAEpuGgSQZpq1tB_znEL485_FsTHOMlRdfQ')

#Кнопки, появляющиеся при запуске бота и после нажатия кнопки «Назад».
markup_help = types.ReplyKeyboardMarkup()

mainbutton = types.KeyboardButton("Основной функционал бота")
groupbutton = types.KeyboardButton("Авторы бота")
techdocbutton = types.KeyboardButton("Техническая документация бота (пока не работает)")
presentbutton = types.KeyboardButton("Презентация про страдания с ботом (пока не работает)")

#Распределение кнопок по рядам.
markup_help.row(mainbutton)
markup_help.row(groupbutton, techdocbutton, presentbutton)

#Кнопки, появляющиеся при нажатии кнопки «Основной функционал бота».
markup_docs = types.ReplyKeyboardMarkup()

mapbutton = types.KeyboardButton("Карта университета")
guidebacbutton = types.KeyboardButton("Путеводитель бакалавра")
calendarbutton = types.KeyboardButton("Академический календарь")
rupbutton = types.KeyboardButton("РУПы и учебные программы")
miscbutton = types.KeyboardButton("Назад")

#Распределение кнопок по рядам.
markup_docs.row(mapbutton, guidebacbutton)
markup_docs.row(calendarbutton)
markup_docs.row(rupbutton, miscbutton)

#Обработка команды /start и подобных ей синонимов (без понятия, на кой чёрт это нужно, но решил, что будет прикольно).
@bot.message_handler(commands=['start', 'begin', 'начать', 'бастау', 'выход', 'стоп', 'exit', 'stop', 'шығу', 'тоқта'])
def function(message):
    bot.send_message(message.chat.id, f"Здарова, {message.from_user.first_name}! Сегодня не срёшь.", reply_markup=markup_help)

#Обработка простого текста, который идёт без слэшей.
@bot.message_handler()
def main(message):
    if message.text == "Авторы бота":
        bot.send_message(message.chat.id, "Над сим великолепием работали:\nКизатбаева Алуа\nМетельников Демид\nСембаев Дильшат\nХахахахаха, поставьте три, пж.")
    elif message.text == "Основной функционал бота":
        bot.send_message(message.chat.id, "Чем могу вам помочь?", reply_markup=markup_docs)
    elif message.text == "Карта университета":
        #Открытие файла для чтения из директории с кодом бота.
        unimap = open("./unimap.png", "rb")  
        bot.send_photo(message.chat.id, unimap)
        bot.send_message(message.chat.id, "Запомните корпуса, в которых чаще всего будут проходить занятия:\n1. Главный учебный корпус (ГУК) — именно здесь вы подаёте документы в Политех и именно здесь вы будете учиться 90% времени. Большое десятиэтажное здание на пересечении улиц Сатпаева и Байтурсынова. Главный вход — со стороны улицы Байтурсынова.\n2. Горно-металлургический корпус — самый старый, но оттого не менее красивый и оснащённый корпус университета. Здесь, помимо учебных аудиторий и научных лабораторий, находятся спортзал, актовый зал и многие студенческие организации (например, студенческая филармония).\n3. Нефтяной корпус (НК) — чилл и раслабон, второй по величине корпус университета. В нём обитает значительная часть администрации университета, а также бухгалтерия, IT-отдел и офис международных отношений.")
    elif message.text == "Путеводитель бакалавра":
        bot.send_message(message.chat.id, "Файл сравнительно большой, может долго загружаться. Пожалуйста, подождите...")
        #Открытие файла из директории с кодом бота.
        guidebac = open("./bachelor.pdf", "rb")
        bot.send_document(message.chat.id, guidebac)
        bot.send_message(message.chat.id, "<b>Внимание!</b> Этот документ — для студентов бакалавриата. Документов для магистров или докторантов ещё не завезли, извиняйте)", parse_mode="html")
    elif message.text == "Академический календарь":
        #Открытие файла из директории с кодом бота.
        calendar = open("./calendar.pdf", 'rb')
        bot.send_document(message.chat.id, calendar)
        bot.send_message(message.chat.id, "<b>Внимание!</b> Этот документ — для студентов бакалавриата. Документов для магистров или докторантов ещё не завезли, извиняйте)", parse_mode="html")
    elif message.text == "РУПы и учебные программы":
        bot.send_message(message.chat.id, "К сожалению, нам лень выгружать каждую учебную программу и делать для них варианты выбора, так что ограничимся лишь РУПом по специальности Computer Science.")
        #Открытие файла из директории с кодом бота.
        rup = open("./CS_rup.pdf", 'rb')
        bot.send_document(message.chat.id, rup)
    elif message.text == "Назад":
        bot.send_message(message.chat.id, "Сегодня всё ещё не срёшь.", reply_markup=markup_help)

#Команда, благодаря которой бот работает постоянно и не крашится на каждом шагу.
bot.infinity_polling()
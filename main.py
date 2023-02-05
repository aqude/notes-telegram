import connect_db
import telebot

# подключаемся к базе данных
db = connect_db.ConnectDB()
tg = connect_db.tg_token()
# подключаемся к боту
bot = telebot.TeleBot(tg)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '''
    Привет, я бот, который поможет тебе записывать заметки
    Чтобы узнать список команд, введи /help
    ''')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, '''
    /add - добавить заметку;\n/list - просмотреть список заметок;\n/list date - просмотреть список с датой;
    ''')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '/add':
        msg = bot.send_message(message.chat.id, "Введите вашу заметку:")
        bot.register_next_step_handler(msg, add_note)
    elif message.text == '/list':
        bot.send_message(message.chat.id, "Вот ваши заметки:")
        list_note(message)
    else:
        pass


def add_note(message):
    note = message.text
    db.write_db(note)
    bot.send_message(message.chat.id, "Заметка добавлена")


def list_note(message):
    notes = db.read_db()
    bot.send_message(message.chat.id, notes)


bot.infinity_polling()

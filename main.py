import connect_db
import telebot

# подключаемся к базе данных
db = connect_db.ConnectDB()

# подключаемся к боту
bot = telebot.TeleBot(db.tg_token())


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '''
    Привет, я бот, который поможет тебе записывать заметки
    Чтобы узнать список команд, введи /help
    ''')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, '''
    /add - добавить заметку;
    /list (full/''*)- просмотреть список заметок;    
    
                                   
    * - просмотреть только заметки;
    full - просмотреть заметки с датой;
    ''')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '/add':
        msg = bot.send_message(message.chat.id, "Введите вашу заметку:")
        bot.register_next_step_handler(msg, add_note)
    elif message.text == '/list':
        msg = bot.send_message(message.chat.id, "Вот ваши заметки:")
        bot.register_next_step_handler(msg, list_note)
    else:
        pass


def add_note(message):
    note = message.text
    db.write_db(note)
    bot.send_message(message.chat.id, "Заметка добавлена")


def list_note(message, full=False):
    notesFull = db.read_db_full()
    notes = db.read_db()
    if full:
        bot.send_message(message.chat.id, "".join(notesFull))
    else:
        bot.send_message(message.chat.id, "".join(notes))


bot.infinity_polling()

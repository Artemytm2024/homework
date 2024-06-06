import telebot
import random

# Токен, полученный от @BotFather - необходимо указать свой токен
TOKEN = 'TOKEN'

# Определяем варианты вопросы от пользователя, на которые бот сможет отвечать
user_questions = [
    "как дела",
    "как дела?",
    "как твои дела",
    "как твои дела?"
    ]

# Определяем несколько вариантов ответа
bot_answers = [
    "Спасибо что спросили. У меня все отлично!",
    "Сложно сказать, я ведь просто программа. Но метавизируя абстракцию, могу предположить, что неплохо - я работаю! ",
    "Здорово! Великолепно!"
    ]

# Инициализируем бота
bot = telebot.TeleBot(TOKEN)

# Функция отправляет приветствие при получении команды /start от пользователя
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, на связи бот. Я могу рассказать, как у меня дела!")

# Функция отвечает на вопрос "как дела" случайным ответом, на другие сообщения отвечает одним и тем же текстом.
@bot.message_handler(func=lambda message: True)
def send_status(message):
    if message.text.lower() in user_questions:
        bot_answer = random.choice(bot_answers) #выбираем случайный ответ из bot_answers
    else:
        bot_answer = "Я пока не понимаю. Лучше спросите, как у меня дела!"
    bot.reply_to(message, bot_answer)


# Запуск бота
def bot_start_polling():
    bot.polling()
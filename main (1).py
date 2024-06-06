from functions import bot_start_polling

def start():
    print("Запуск бота")
    bot_start_polling()
    print("Остановка бота")

if __name__ == '__main__':
    start()
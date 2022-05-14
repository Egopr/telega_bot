import telebot
bot = telebot.TeleBot('5381690103:AAHNocBE6yxMM3sL2Lx_Abji76RTCaFvU-g')
'''
kb1 = telebot.types.ReplyKeyboardMarkup(True)
kb1.row('Хуй', 'Пизда')
kb1.row('Джигурда','Анал')
kb1.row('Парашют','ДДЮТ')
'''
#Запись данных из листа в файл, с разделителем "запятая".
all_date = []
def in_file_data(data_user):
    data_users = open("data.csv", "a+t")
    for i in range(len(data_user)):
        data_users.writelines(data_user[i])
        if i < (len(data_user) - 1):
            data_users.write(', ')
    data_users.write('\n')
    data_users.close()


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, 'Готов вам помочь, что бы вы хотели ?')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def sbor_text(message):
    sent = bot.send_message(message.chat.id,'Введите Имя')
    bot.register_next_step_handler(sent, get_name)

def get_name(m): #Функция записи имени и перевод на функцию записи фамилии
    name = m.text
    all_date.append(name)
    bot.send_message(m.chat.id, 'Ваше имя записано')
    sent = bot.send_message(m.chat.id, 'Теперь введите свою фамилию')
    bot.register_next_step_handler(sent, get_surname)

def get_surname(message): # Функция записи фамилии и перевод на функцию ___
    surname = message.text
    all_date.append(surname)
    bot.send_message(message.chat.id, 'Ваше фамилия записана')
    print(all_date)
    in_file_data(all_date)
    all_date.clear()

    #sent = bot.send_message(message.chat.id, 'Ваше имя записано')
    #bot.register_next_step_handler(sent, get_surname)




# Запускаем бота
bot.polling(none_stop=True, interval=25)

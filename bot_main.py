from config import TOKEN
from config import questions
from config import options


import telebot
import logging
import sys

from scorer import display_score
from data_base_user import add_to_bd


logger = telebot.logger
formatter = logging.Formatter('[%(asctime)s] %(thread)d {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
                              '%m-%d %H:%M:%S')
ch = logging.StreamHandler(sys.stdout)
logger.addHandler(ch)
logger.setLevel(logging.INFO)  # or use logging.INFO
ch.setFormatter(formatter)


# -------------------------

question_num = 0
guesses = []


# -------------------------


def tbot(token):
    bot = telebot.TeleBot(token)
    print("bot is online")

    @bot.message_handler(commands=['start'])
    def start_message(message):
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard1.row('Начать тест')

        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помочь вам выбрать инвест профиль".format(message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=keyboard1)


# -------------------------

    @bot.message_handler()
    def starttest(message):  # Название функции не играет никакой роли
        if message.text == "Начать тест":
            global question_num
            remover = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, "Сейчас я задам вам несколько вопросов, отвечайте A, B, C или D. Если вы не бывали в той или иной ситуации, ответьте гипотетически. Тест анонимен для разработчиков, отвечайте максимально честно.", reply_markup=remover)
            question_num = 0
            start_testing(message)

    def start_testing(message):
        global question_num
        global questions
        global options

        keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard2.row('A', 'B')
        keyboard2.row('C', 'D')

        index = questions[question_num]
        print('question ' + str(question_num))

        bot.send_message(message.chat.id, index, reply_markup=keyboard2)

        for i in options[question_num]:
            bot.send_message(message.chat.id, i)

        print(message.text)
        bot.register_next_step_handler(message, get_answer)

# -------------------------

    def get_answer(message):
        global question_num
        global guesses
        global guess

        print('getting answer')
        guess = message.text
        guess = guess.upper()

        if guess == "A" or guess == "B" or guess == "C" or guess == "D":

            guesses.append(guess)

        else:

            guesses.append("invald answer")

        question_num += 1
        print(question_num)

        if question_num == 11:

            all_user_info = " "
            usid = " "

            print('quiz ended')

            result = display_score(guesses=guesses)
            print(result)

            remover = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, str(
                result), reply_markup=remover)

            bot.send_message(
                message.chat.id, 'Не является инвестиционной рекомендацией, данный тест составлен на базе мнения разработчиков')

            if message.from_user.last_name != None and message.from_user.username != None and usid != None:
                all_user_info = message.from_user.first_name + '-' + \
                    message.from_user.last_name + '-' + message.from_user.username
            usid = message.chat.id
            gu_str = str(guesses)

            print(usid, gu_str, all_user_info)
            add_to_bd(usid, gu_str, all_user_info)

            all_user_info = None
            usid = None
            gu_str = None

        else:

            start_testing(message)

# -------------------------

    bot.polling()

# -------------------------


if __name__ == '__main__':
    tbot(TOKEN)

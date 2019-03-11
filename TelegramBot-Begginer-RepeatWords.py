# in config we store token id in format token = ''
# telebot is a Python implementaiton of Bot API: https://github.com/eternnoir/pyTelegramBotAPI
# Functionality: Bot repeats your message

import config
import telebot

bot=telebot.TeleBot(config.token)

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message( message.chat.id, message.text)
if __name__ == '__main__':
    bot .polling(none_stop=True)

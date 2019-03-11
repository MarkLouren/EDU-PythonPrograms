# use Liabrary: https://github.com/python-telegram-bot/python-telegram-bot

from telegram.ext import Updater, CommandHandler
import requests
import re

# using public Api get Json data from the site random.dog
def get_url():
    contents=requests.get('https://random.dog/woof.json').json()
    url=contents['url']
    return url
# send an image
# chat_id = update.message.chat_id

def dog(bot, update):
    url =get_url() #from the previous function
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('tokenId') #bot token
    db = updater.dispatcher  #send a message
    db.add_handler(CommandHandler('dog', dog))#command Dog
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':   #launch bot
    main()

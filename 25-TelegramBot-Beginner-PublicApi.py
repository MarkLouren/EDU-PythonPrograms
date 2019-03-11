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

def get_image_url():  # chose only jpg in urls, because telegram not supports Gif
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def dog(bot, update):
    url =get_image_url() #from the previous function
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('tokenid') #bot token
    db = updater.dispatcher  #send message
    db.add_handler(CommandHandler('dog', dog))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

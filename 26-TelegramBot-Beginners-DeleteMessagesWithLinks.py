#Delete new mesages that contain links in chats
# Tutotial in Ru:  https://groosha.gitbooks.io/telegram-bot-lessons/content/chapter10.html 
import telebot
bot = telebot.TeleBot('tokenid')

GROUP_ID = -1001288763948  # Your group Id

@bot.message_handler(func=lambda message: message.entities is not None and message.chat.id == GROUP_ID)
def delete_links(message):
    for entity in message.entities:  # check all # entities looking for linkd
        # url - link, text_link - text link
        if entity.type in ["url", "text_link"]:
            # we can't check chat.id, it' checked in handler
            bot.delete_message(message.chat.id, message.message_id)
        else:
            return

if __name__ == '__main__':
    bot.polling(none_stop=True) # run bot permanently 

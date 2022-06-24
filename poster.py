import telebot
import sys
import os

try:
  
  chat_id = int(sys.argv[1])
  file = str(chat_id)+'.png'
  bot = telebot.TeleBot("5517829609:AAH5ZJif7DVNrUDD5-XAtacvhh7rps1wczY")
  img = open(file, 'rb')
  bot.send_photo(chat_id, img)
  os.remove(file)

except:
  pass

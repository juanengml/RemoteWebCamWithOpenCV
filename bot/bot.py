# -*- coding: utf-8 -*-

import sys
import time
import telepot
from telepot.loop import MessageLoop
import numpy as np
import pandas as pd
import os

std = """Oi, sou um bot que avisa quem esta na sua casa """

TOKEN = " 131231231313 "

img_path = "../webapp/face.jpg"


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    
    if content_type == 'text':
    	print msg['text']
    	if msg['text'] == "Oi":
          bot.sendMessage(chat_id, std)

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
chat_id = 123
while 1:
    face = int(os.popen("cat status.txt").read().split()[0])
    if face == 1:
     bot.sendMessage(chat_id, "Face Detectada")
     print "Face Detectada"
     try:
         bot.sendPhoto(chat_id,open(img_path, 'rb'))
         print "Face Detectada"
     except:
         bot.sendPhoto(chat_id,open(img_path, 'rb'))
         print "Face Detectada"
     else:
         bot.sendPhoto(chat_id,open(img_path, 'rb'))
         print "Face Detectada"
     finally:
         bot.sendPhoto(chat_id,open(img_path, 'rb'))
         print "Face Detectada"
     
     time.sleep(5)
    else:
        print '.'
        time.sleep(5)

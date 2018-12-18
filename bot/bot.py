# -*- coding: utf-8 -*-

import sys
import time
import telepot
from telepot.loop import MessageLoop
import numpy as np
import pandas as pd
import os

std = """Oi, sou um bot que avisa quem esta na sua casa """

TOKEN = "744893793:AAGkn_KA3Huq1IQFIojWXZ2x4pb7LRh0Ixc"

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

while 1:
    face = int(os.popen("cat status.txt").read().split()[0])
    if face == 1:
     bot.sendMessage("120773442", "Face Detectada")
     print "Face Detectada"
     try:
         bot.sendPhoto("120773442",open(img_path, 'rb'))
         print "Face Detectada"
     except:
         bot.sendPhoto("120773442",open(img_path, 'rb'))
         print "Face Detectada"
     else:
         bot.sendPhoto("120773442",open(img_path, 'rb'))
         print "Face Detectada"
     finally:
         bot.sendPhoto("120773442",open(img_path, 'rb'))
         print "Face Detectada"
     
     time.sleep(5)
    else:
        print '.'
        time.sleep(5)

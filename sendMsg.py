# -*- coding: utf-8 -*-
import telepot
import json
import datetime
import time

token = ""
bot = telepot.Bot(token)


def send(res):
    bot.sendMessage(chat_id='', text="<a href='https://upbit.com/service_center/notice?id="+str(res['id'])+"'>"+res['title']+"</a>", disable_web_page_preview=True, parse_mode='HTML')


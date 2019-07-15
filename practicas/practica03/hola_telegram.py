#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# Alumno: David Rodriguez Alonso
# Login: alonsod

import sys, os
import telepot
import telepot.namedtuple
import time
from telepot.loop import MessageLoop

def read_token():
    try:
        fd = open("token.txt")
    except IOError:
        sys.stderr.write("Error: cannot open token.txt\n")
        exit(1)
    try:
        token = fd.readline()
    except IOError:
        sys.stderr.write("Error: cannot read token.txt\n")
        exit(1)

    fd.close()
    return token

def init_bot():
    TOKEN = read_token()    # get token from file token.txt
    bot = telepot.Bot(TOKEN)
    return bot

bot = init_bot() # variable bot must be global for function MessageLoop

def handle(msg):
    chat_id = msg["chat"]["id"]
    texto = msg["text"]
    print msg
    print "\n"

    if texto == "/start":
        bot.sendMessage(chat_id, "Hello there! Welcome to alonsod's bot. Type any message to have a reply. Enjoy!")
    else:
        respuesta = "Has escrito " + texto.lower()
        bot.sendMessage(chat_id, respuesta)
    return


def main():
    MessageLoop(bot, handle).run_as_thread()
    print "Listenning client...\n"

    while True:
        time.sleep(10)
    return

if __name__ == "__main__":
    main()

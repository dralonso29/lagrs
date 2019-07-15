#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# Alumno: David Rodriguez Alonso
# Login: alonsod

import sys, os, subprocess
import telepot
import telepot.namedtuple
import time
from telepot.loop import MessageLoop
import time,datetime, pytz, calendar;

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

def exec_command(command):
    command_splitted = command.split()
    command_splitted[0] = command_splitted[0].lower()
    try:
        result = subprocess.check_output(command_splitted)
    except Exception as e:
        result = "Sorry, command " + command + " can't be executed"
    return result

def printtimeepoch(date):
    dt = datetime.datetime.utcfromtimestamp(float(date)); # pasamos el timestamp a date naive
    ciudad = pytz.timezone("Europe/Madrid");
    dt = pytz.utc.localize(dt);   #vinculamos la date naive a utc primero
    dt = dt.astimezone(ciudad); # luego le asignamos su ciudad (la del fichero)
    return dt

def print_stdout(msg):
    print "Fecha: " + str(printtimeepoch(msg["date"]))
    print "Complete name: " + msg["from"]["first_name"] + " " + msg["from"]["last_name"]
    print "User: " + msg["from"]["username"]
    print "User ID " + str(msg["from"]["id"])
    print "Message: " + msg["text"]
    print "\n"

def handle(msg):
    chat_id = msg["chat"]["id"]
    texto = msg["text"]
    print_stdout(msg)

    if texto == "/start":
        bot.sendMessage(chat_id, "Hello there! Type any shell command and see the result. Enjoy!")
    elif texto == ("/stop" or "Stop" or "stop" or "Salir" or "salir"):
        bot.sendMessage(chat_id, "Hope you really enjoyed. See you next time")
    else:
        texto = texto.lower()
        respuesta = exec_command(texto)
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

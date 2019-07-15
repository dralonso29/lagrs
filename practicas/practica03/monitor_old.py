#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# Alumno: David Rodriguez Alonso
# Login: alonsod

from optparse import OptionParser
import sys, os, subprocess
import telepot
import telepot.namedtuple
import time
from telepot.loop import MessageLoop
import time,datetime, pytz, calendar

DIRECTORIOS = ["~lagrs/test01", "~/lagrs/test02", "~/lagrs/test03", "~/lagrs/test04"]
#DIRECTORIOS = ["/tmp/prueba/todo_ok", "/tmp/prueba/mal_files", "/tmp/prueba/mal_size", "/tmp/prueba/mal_all"]
MAX_TAMANIO = 2 # Mb
MAX_FICHEROS = 3
ID_USUARIO = 138327167
MILLION = 1000000

def read_token():
    try:
        fd = open("./token.txt")
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
    try:
        result = subprocess.check_output(command_splitted)
    except Exception as e:
        sys.stderr.write("Error while subprocess command " + command + "\n")
        exit(1)
    return result

def size_and_total(lines):
    total_size = 0
    total_files = 0
    for line in lines:
        field = line.split()
        total_files += 1
        total_size += float(field[4])
    return total_size, total_files

def convert_to_Mb(size):
    return (size)/MILLION

def send_messages(dirname, size, nfiles, force):
    size = convert_to_Mb(size)
    flag = True
    if size > MAX_TAMANIO and nfiles > MAX_FICHEROS:
        flag = False
        msg_error_all = "Warning: in dir "+ dirname + ":\nBad total size: " + \
        str(size) +" > "+ str(MAX_TAMANIO)+ "\nBad total files: " + \
        str(nfiles)+" > "+str(MAX_FICHEROS) + "\n"
        print msg_error_all
        bot.sendMessage(ID_USUARIO, msg_error_all)
    elif size > MAX_TAMANIO:
        flag = False
        msg_error_size = "Warning: in dir "+ dirname + ":\nBad total size: " + \
        str(size) +" > "+ str(MAX_TAMANIO)+"\n"
        print msg_error_size
        bot.sendMessage(ID_USUARIO, msg_error_size)
    elif nfiles > MAX_FICHEROS:
        flag = False
        msg_error_files = "Warning: in dir "+ dirname + ":\nBad total files: " + \
        str(nfiles)+" > "+str(MAX_FICHEROS) + "\n"
        print msg_error_files
        bot.sendMessage(ID_USUARIO, msg_error_files)
    if force and flag:
        msg_ok = "All is ok in dir " + dirname + "\n"
        print msg_ok
        bot.sendMessage(ID_USUARIO, msg_ok)

def prepare_dirname(dirname):
    virgulilla = "~"
    virgulilla2 = "~/"
    two = "//"
    one = "/"
    if dirname.find(virgulilla) >= 0 or dirname.find(virgulilla2) >= 0:
        dirname = dirname.replace(virgulilla, virgulilla2)
        path = os.path.expanduser(virgulilla)
        dirname = dirname.replace(virgulilla, path)
        dirname = dirname.replace(two, one)
    return dirname

def prepare_bot(force):
    for dirname in DIRECTORIOS:
        command = "ls -l "
        dirname = prepare_dirname(dirname)
        command = command + dirname
        myresult = exec_command(command)
        lines = myresult.split("\n")  #split the result of command by \n
        lines.pop(0)    #we will not use the header
        lines.pop()     #and the last line because its an empty line
        size, nfiles = size_and_total(lines) # return total size in Mb and total files on dir
        send_messages(dirname, size, nfiles, force)

def main():
    argc = len(sys.argv);
    usage = "Usage: " + sys.argv[0] + " [options]\n"
    parser = OptionParser()
    parser.add_option("-f", "--force-telegram", action="store_true", dest="force",
                        help="forces message if all is ok or not")
    options, args = parser.parse_args()

    if argc > 2:
        sys.stderr.write(usage)
        exit(1)
    prepare_bot(options.force) # if user entered -f, options.force = True. In other case,  options.force = None

if __name__ == "__main__":
    main()

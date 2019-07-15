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

MAQUINAS = ["alpha01", "alpha02"]
COMANDOS = ["touch /tmp/log_monitoriza_alonsod.txt", "~/lagrs/practica03/monitor.py --force-telegram"]
# MAQUINAS = ["8.8.8.8", "127.0.0.1"]
# COMANDOS = ["touch /tmp/log_monitoriza.txt", "echo 1234 >> /tmp/pueba.txt"]

def ping_works(pc):
    cmd = "ping -c 1 -W 3 "
    cmd += pc
    command_splitted = cmd.split()
    FNULL = open(os.devnull, 'w')
    try:
        result = subprocess.check_call(command_splitted, stdout=FNULL, stderr=FNULL)
    except Exception as e:
        sys.stderr.write("Error while subprocess command " + cmd + "\n")
        exit(1)
    return result

def exec_cmds(maquina, comandos):
    for comando in comandos:
        myssh = "ssh alonsod@"
        myssh += maquina + " "
        myssh += comando
        myssh = myssh.split()
        try:
            result = subprocess.check_output(myssh)
        except Exception as e:
            sys.stderr.write("Error while subprocess command " + str(myssh) + "\n")
            exit(1)

def main():
    argc = len(sys.argv)
    usage = "Usage: " + sys.argv[0] + " [options]\n"
    if argc > 1:
        sys.stderr.write(usage)
        exit(1)
    for pc in MAQUINAS:
        if ping_works(pc) == 0: #if ping on pc worked
            exec_cmds(pc, COMANDOS)

if __name__ == "__main__":
    main()

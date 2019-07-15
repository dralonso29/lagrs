#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# Alumno: David Rodriguez Alonso
# Login: alonsod

import subprocess, sys, os
from stat import *

def exec_command(command):
    command_splitted = command.split()
    try:
        result = subprocess.check_output(command_splitted)
    except Exception as e:
        sys.stderr.write("Error while subprocess command " + command + "\n")
        exit(1)
    return result

def show_result(result):
    lines = result.split("\n")  #split the result of command by \n
    lines.pop(0)    #we will not use the header
    lines.pop()     #and the last line because its an empty line
    for line in lines:
        fields = line.split()   # split by space
        name = "./"+fields[8]   # make the path of every element of actual dir
        try:
            mode = os.stat(name).st_mode
        except Exception as e:
            sys.stderr.write("Error: stat failed with path or name " + fields[8] + "\n")
            exit(1)

        if S_ISREG(mode):   # if it's regular file, print its name and size
            print fields[8] + " " + fields[4]

def main():
    command = "ls -l"
    result = exec_command(command)
    show_result(result)
    exit(0)

if __name__ == "__main__":
    main()

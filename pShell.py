#!/usr/bin/python
import sys
import pwd
import subprocess

import os
from os import stat
import datetime
os.system('clear')
print("----------------------------------------------------------------------\n"
      "                       Welcome to custom pShell\n"
      "----------------------------------------------------------------------\n")


#function for showing history
def history():
    for history in open('/home/Ted/.bash_history'):
        print(history)

#function for getting present working directory
def pwd():

    path = subprocess.check_output('pwd').strip()
    print(path)
    return

# function for getting information of a inteface specfied by the user

def interface(response):
    if '01' in response:
        print(os.system('ifconfig eth01'))
    elif '02' in response:
        print(os.system('ifconfig eth02'))
    elif 'lo' in response:
        print(os.system('ifconfig ethlo'))
    else:
        print(os.system('ifconfig'))
    return

# function for date & time

def dateT():

    print(os.system('date'))

# function for user id,groupid, usernam

def userInfo():


    gid = os.system("id -g")
    uid = os.system("id -u -n")
    groups = os.system("id")
    inode = stat("/home/user").st_ino

    print("groupid is {}").format(gid)
    print("user is {}").format(uid)
    print("groups {}").format(groups)
    print(inode)


# function to exit shell if user chooses to

def exitS():
    sys.exit()

# function to display --help to the user
# displays list of commands available in this custom shell

def helpF():
    exit = "exit"
    pwd = "pw"
    ifc = "ifc"
    date = "dt"
    user = "ud"
    history = "history"
    logs = "login history"

    print("{}    ---- exits the shell").format(exit)
    print("{}    ---- parent working directory").format(pwd)
    print("{}    ---- ifconfig").format(ifc)
    print("{}    ---- date").format(date)
    print("{}    ---- user details").format(user)
    print("{}    ---- command history").format(history)
    print("{}    ---- login logs").format(logs)

    return

#function for reading authenticated users logged on

def logAuth():

    with open('/var/log/auth.log') as f:
        while True:
            line = f.readline()
            if line:
               print (line)

while True:

    response = raw_input("#pShell--$")

    if response == "pw":
        pwd()
    elif response == "ifc" or response== "ifc01" or response == "ifc02" or response == "ifclo":
        interface(response)
    elif response == "dt":
        dateT()

    elif response == "ud":
        userInfo()
    elif response == "exit":
        exitS()
    elif response == "help":
        helpF()
    elif response == "logs":
        logAuth()
    elif response =="history":
        history()
    else:
        print("{}: command not found").format(response)

#!/bin/python3

## import modules
import getpass
from datetime import datetime
import os

## variables
username = getpass.getuser()
date_now = datetime.now()
date_time = date_now.strftime("%d.%m.%Y %H:%M:%S")
cwd = os.getcwd()

## greeting-function
def say_hello(username):
    print("Hallo " + username)
    print("Es ist der " + date_time +" Uhr")
    print("Current Working Directory " + cwd)

## call function
say_hello(username)

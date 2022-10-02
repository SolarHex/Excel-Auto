import random
from getpass import getpass
from openpyxl import workbook
from openpyxl.reader.excel import load_workbook
from openpyxl.workbook.workbook import Workbook

nick = input('You Nickname: ')
psw = getpass('You password: ')

if len(psw) <6:
    err = input('It is narrow, we can help you create new password. Do you wanna?(Yes/No)')
    if err == 'Yes':
        randpass = ''.join([random.choice(list('qwerasdfzxcvbgthynmjuiklopZAQWSXCDEVFRGTHBYNJUIKLOMP123456789')) for i in range(7)])
        print(randpass)
    else:
        psw = getpass(input('You password: '))

print(nick,psw)
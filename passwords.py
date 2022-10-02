import random 
from openpyxl import workbook
from openpyxl.reader.excel import load_workbook
from openpyxl.workbook.workbook import Workbook

nick = input("You username: ")
passw = input("You password: ")

if len(passw) < 6:
        err = input('It is narrow, we can help you create new password. Do you wanna?(Yes/No)')
        if err == 'Yes':
            randpass = ''.join([random.choice(list('qwerasdfzxcvbgthynmjuiklopZAQWSXCDEVFRGTHBYNJUIKLOMP123456789')) for i in range(7)])
            print(f"{randpass} is you new password!")
        else:
            while True:
                new_passw = input('You password: ')
                if len(new_passw) > 6:
                    print("You password is good!")
                    break
                
else:
    print("You password is good!")

wb = Workbook()
ws=wb.active

data = {
    '1':{
        "Username":nick,
        "Password":passw
    }
}

headings = ["№"] + list(data['1'].keys())
ws.append(headings)

for i in data:
    pep = list(data[i].values())
    ws.append([i]+pep)


wb.save("DATA.xlsx")
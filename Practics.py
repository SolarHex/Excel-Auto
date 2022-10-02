from openpyxl import workbook
from openpyxl.reader.excel import load_workbook
from openpyxl.workbook.workbook import Workbook
import random

wb = Workbook()
ws = wb.active

day = random.randint(1,31)
month =  random.randint(1,12)
year = random.randint(2018,2021)
day1 = random.randint(1,31)
month1 =  random.randint(1,12)
year1 = random.randint(2018,2021)
day2 = random.randint(1,31)
month2 =  random.randint(1,12)
year2 = random.randint(2018,2021)
day3 = random.randint(1,31)
month3 =  random.randint(1,12)
year3 = random.randint(2018,2021)
day4 = random.randint(1,31)
month4 =  random.randint(1,12)
year4 = random.randint(2018,2021)

c = random.randint(1,10)
c1 = random.randint(1,10)
c2 = random.randint(1,10)
c3 = random.randint(1,10)
c4 = random.randint(1,10)

a = random.randint(1,10)
a1 = random.randint(1,10)
a2 = random.randint(1,10)
a3 = random.randint(1,10)
a4 = random.randint(1,10)



data = {
    '1':{
        "DATE":day,
        "Month":month,
        "Year":year,
        "Code": c,
        "Surname": "Sergio",
        "Code of book": c,
        "Purchase":"Backpack",
        "Amount of Purchase": a,
        "Sum": a*c
    },
    '2':{
        "DATE":day1, 
        "Month":month1, 
        "Year":year1,
        "Code": c1,
        "Surname": "Domodedov",
        "Code of book": c1,
        "Purchase":"Pencil",
        "Amount of Purchase": a1,
        "Sum": a1*c1
    },
    '3':{
        "DATE":day2,
        "Month":month2, 
        "Year":year2,
        "Code": c2,
        "Surname": "Zarechniy",
        "Code of book": c2,
        "Purchase":"Pen",
        "Amount of Purchase": a2,
        "Sum": a2*c2
    },
    '4':{
        "DATE":day3, 
        "Month":month3, 
        "Year":year3,
        "Code": c3,
        "Surname": "Nagorniy",
        "Code of book": c3,
        "Purchase":"Watch for study",
        "Amount of Purchase": a3,
        "Sum": a3*c3
    },
    '5':{
        "DATE":day4, 
        "Month":month4, 
        "Year":year4,
        "Code": c4,
        "Surname": "Tverskoy",
        "Code of book": c4,
        "Purchase":"Albom for drawings",
        "Amount of Purchase": a4,
        "Sum": a4*c4
    }
}

headings = ['№'] + list(data['1'].keys())
ws.append(headings)

for i in data:
    pep = list(data[i].values())
    ws.append([i]+pep)
    
wb.save('Practica for students.xlsx')
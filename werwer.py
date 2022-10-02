import random 
from getpass import getpass
from openpyxl import workbook
from openpyxl.reader.excel import load_workbook
from openpyxl.workbook.workbook import Workbook

passw = input("You password: ")
print(len(passw))
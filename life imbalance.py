# создаем список букв
import string
list(string.ascii_lowercase)
alphabet = list(string.ascii_lowercase)

# генерация словаря
d = {val:idx for idx,val in enumerate(alphabet)}
print(d)
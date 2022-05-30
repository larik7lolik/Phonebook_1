from datetime import datetime
import datetime

def record():
   entry=[]
   surname = input('\nВведите Фамилию: ')
   entry.append(surname.title())
   name = input('Введите Имя: ')
   entry.append(name.title())
   telefon = input('Введите номер телефона: ')
   entry.append(telefon.title())
   description = input('Введите описание контакта(личный, рабочий, домашний и т.д.): ')
   entry.append(description.title())
   dt = datetime.datetime.now()
   entry.insert(0,dt.strftime('%H:%M - %d.%m.%Y year'))
   print('Вами введена запись: ', entry)
   return entry
    
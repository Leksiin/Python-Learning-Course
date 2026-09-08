"""collection = [] #list
is_start = True #flag

while (is_start):
    print("1 - показать заметки | 2 - добавить заметку")
    choice_user = input('Введите ваш выбор (1 или 2)')
    match int(choice_user):
        case 1:
            print(collection)
        case 2:
            collection.append('task')
            print(collection)
        case _:
            print('Такого пункта нет!')"""

"""import os
import sys
import platform
import datetime

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]
os_processor = platform.processor()
os_machine = platform.machine()
os_python_version = platform.python_version()
os_android = platform.android_ver()

now = datetime.datetime.now()
sys_in = sys.path
sys_platform = sys.platform
sys_version = sys.version

print(f"{os_name} \n" 
      f"{os_version} \n" 
      f"{os_arch} \n" 
      f"{now.year} \n" 
      f"{now.month} \n" 
      f"{now.day} \n" 
      f"{now.hour} \n"
      f"{now.minute} \n"
      f"{now.second} \n"
      f"{now.microsecond} \n" 
      f"{os_processor} \n" 
      f"{os_machine} \n" 
      f"{os_python_version} \n" 
      f"{os_android} \n")"""

"""Код выводит данные компьютера, такие как его имя, версия оп, время и т.д."""
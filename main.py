"""1.
collection = [] #list
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
            print('Такого пункта нет!')

2.
import os
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
      f"{os_android} \n")

Код выводит данные компьютера, такие как его имя, версия оп, время и т.д.



 Приложение Task Manager
==============================================================
    Консольное приложение - менеджер управления заметок,
    пользователь может создать заметки, редактировать,
    посмотреть все заметки или удалить выбранную.
==============================================================
~~~~~~~~~~~~~~~~~~~~~
| version app 0.0.7 |
~~~~~~~~~~~~~~~~~~~~~

v(0.0.1)
Разработан цикл приложения - структурное программирование

v(0.0.2)
Внедрен i/o функционал для ввода задачи

v(0.0.3)
Разработаны функции для цикла - функциональное программирование

v(0.0.4)
Добалвены проверки и подтверждения

v(0.0.5)
Созданы методы сохранения и загрузки - файловые сохранения

v(0.0.6)
Созданы методы для удаления, редактирования и создания задач - логика вынесена из цикла

v(0.0.7)
Основной цикл помещён в отдельный метод - def main

v(0.0.8)
Реализован функционал добавления контента задачи - имя + содержание

v(0.0.9)
Созданы модули приложения

v(0.1.0)
Подготовка документации, сборка билда
"""

# import processes

import app

if __name__ == "__main__":
    app.app()

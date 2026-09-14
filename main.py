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

Код выводит данные компьютера, такие как его имя, версия оп, время и т.д."""

is_running = True
collection = [ "task1", "task2" ] # list

def show_collection(task_collection):
    print("=" * 30)
    for i, j in enumerate(task_collection):
        print(i + 1, j)
    print("=" * 30)

def show_menu():
    print("1 - посмотреть задачи \n"
          "2 - добавить задачу \n"
          "3 - редактировать задачу \n"
          "4 - удалить задачу \n"
          "5 - выход")

print("Добро пожаловать!")
while is_running:
    show_menu()
    choice_user = input("Введите свой выбор: ")
    match str(choice_user):
        case '1':
            show_collection(collection)
            waite = input("Нажмите 'ENTER' для продолжения")
        case '2':
            add_task = input("Введите имя задачи для добавления: ")
            if add_task.startswith(' '):
                if len(add_task) < 2:
                    print("Название не может быть пустым!")
                    continue
                else:
                    collection.append(f"Задача {len(collection)}")
            else:
                collection.append(add_task)
        case '3':
            show_collection(collection)
            select_task = input("Введите номер задачи: ")
            if int(select_task.isdigit()):
                if int(select_task) > 0 and int(select_task) <= len(collection):
                    edit_task = input("Введите новое имя задачи для редактирования: ")
                    collection[int(select_task) - 1] = edit_task
                    print(f"Задача '{int(select_task)}' : '{edit_task}' успешно отредактирована!")
                else:
                    print("Задачи с таким номером нет в списке!")
            else:
                print("Введённые данные должны быть номером списка!")
        case '4':
            show_collection(collection)
            delete_task = int(input("Введите номер задачи для удаления: "))
            if int(delete_task) > 0 and delete_task <= len(collection):
                collection.pop(delete_task - 1)
                print(f"Задача '{delete_task}' успешно удалена!")
            else:
                print("Задачи с таким номером нет в списке!")
        case '5':
            is_running = False
            print("До свидания!")
        case _:
            print("Такого пункта нет!")

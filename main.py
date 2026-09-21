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
import os
import processes

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
          "0 - выход")

def show_message():
    input("Нажмите 'ENTER' для продолжения")

def check_confitm(select_task, task_list):
    if select_task.isdigit():
        if (int(select_task) > 0 and int(select_task) <= len(task_list)):
            return 1
        else:
            return 2
    else:
        return 3

def delete_task(task_collection):
    delete_task = input("Введите номер задачи для удаления: ")
    if check_confitm(delete_task, task_collection) == 1:
        task_collection.pop(int(delete_task) - 1)
        print(f"Задача с номером {delete_task} успешно удалена!")
    elif check_confitm(delete_task, task_collection) == 2:
        print(f"Задачи с номером {delete_task} нет в списке!")
    elif check_confitm(delete_task, task_collection) == 3:
        print(f"Введите именно номер задачи!")

def edit_task(task_collection):
    select_task = input("Введите номер задачи: ")
    if check_confitm(select_task, task_collection) == 1:
        edit_name = input("Введите имя задачи")
        task_collection[int(select_task) - 1] = edit_name
        print(f"Задача с номером {edit_name} успешно изменена!")
    elif check_confitm(select_task, task_collection) == 2:
        print(f"Задачи с номером {select_task} нет в списке!")
    elif check_confitm(select_task, task_collection) == 3:
        print(f"Введите именно номер задачи!")

print("Добро пожаловать!")
while is_running:
    show_menu()
    choice_user = input("Введите свой выбор: ")
    match str(choice_user):
        case '1':
            show_collection(collection)
            show_message()
            print (f"TM PID {os.getpid()}")
            print (f"TM PID {os.getppid()}")
            processes.main()

        case '2':
            add_task = input("Введите имя задачи для добавления: ")
            if add_task.startswith(' '):
                if len(add_task) < 2:
                    print("Название не может быть пустым!")
                    continue
                else:
                    collection.append(f"Задача {len(collection) + 1}")
            else:
                collection.append(add_task)
                print(f"Задача '{add_task}' успешно добавлена!")

        case '3':
            show_collection(collection)
            edit_task(collection)

        case '4':
            show_collection(collection)
            delete_task(collection)

        case '0':
            is_running = False
            print("Выход")

        case _:
            print("Такого пункта нет!")

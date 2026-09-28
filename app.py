"""
    ===============================
        Модуль с главным циклом
    ===============================
"""

from storage import load_file, save_file
from view import show_collection, show_menu, show_message
from core import delete_tasks, add_tasks, edit_task
from config import NAME_FILE_SAVES

# Главный цикл приложения
def main():
    is_running = True
    name_file = NAME_FILE_SAVES
    while is_running:
        show_menu()
        choice_user = input("Введите свой выбор: ")
        task_collection = load_file([], name_file)

        match str(choice_user):
            case '1':
                show_collection(task_collection)
                show_message()
                # print (f"TM PID {os.getpid()}")
                # print (f"TM PID {os.getppid()}")
                # processes.main()

            case '2':
                task_collection = add_tasks(task_collection)
                add_tasks(task_collection)
                save_file(task_collection, name_file)

            case '3':
                show_collection(task_collection)
                edit_task(task_collection)
                save_file(task_collection, name_file)

            case '4':
                show_collection(task_collection)
                delete_tasks(task_collection)
                save_file(task_collection, name_file)

            case '0':
                is_running = False
                print("Выход")

            case _:
                print("Такого пункта нет!")

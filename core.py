"""
    =============================================
        Модуль который хранит главные функции
    =============================================
"""

from utils import check_confitm

# Функция удаляющая задачи
def delete_tasks(task_collection):
    delete_task = input("Введите номер задачи для удаления: ")
    if check_confitm(delete_task, task_collection):
        task_collection.pop(int(delete_task) - 1)
        print(f"Задача с номером {delete_task} успешно удалена!")

# Функция редактирующая задачи
def edit_task(task_collection):
    select_task = input("Введите номер задачи: ")
    if check_confitm(select_task, task_collection):
        edit_name = input("Введите имя задачи")
        task_collection[int(select_task) - 1] = edit_name
        print(f"Задача с номером {edit_name} успешно изменена!")

# Функция добавлящая задачи
def add_tasks(task_collection):
    add_task = input("Введите имя задачи для добавления: ")

    # if add_task.startswith(' '):
        # if len(add_task) < 2:
            # print("Название не может быть пустым!")
        # else:
            # task_collection.append(f"Задача {len(task_collection) + 1}")
    # else:
        # task_collection.append(add_task)
        # print(f"Задача '{add_task}' успешно добавлена!")

    task_content = input("Введите содержание задачи")
    if add_task.startswith('') or task_content.startswith(''):
        if len(task_content) < 2 or len(add_task) < 2:
            print(f"Имя задачи и содержание не должно быть пустым!")
    else:
        print(task_collection)
        full_name = f"{add_task} | {task_content}"
        task_collection.append(full_name)
        return task_collection
    return task_collection

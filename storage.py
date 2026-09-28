"""
    ====================================================
        Модуль который загружает и сохраняет задачи
    ====================================================
"""

# Загрузка списка задач из файла
def load_file(task_list, file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            task_list.append(line.strip())
    return task_list

# Сохранение списка зада в файл
def save_file(task_list, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for task in task_list:
            file.writelines(f"{task}\n")

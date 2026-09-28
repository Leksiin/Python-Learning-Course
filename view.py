"""
    ======================================================
        Модуль который отображает информацию в консоли
    ======================================================
"""

# функция для показа списка задач
def show_collection(task_collection):
    print("=" * 30)
    for number, content in enumerate(task_collection):
        for symbol in content:
            word = ''
            if symbol != '|':
                word = f"{word}{symbol}"
            else:
                break
        print(number + 1, str(content))
    print("=" * 30)

# функция для показа меню
def show_menu():
    print("1 - посмотреть задачи \n"
          "2 - добавить задачу \n"
          "3 - редактировать задачу \n"
          "4 - удалить задачу \n"
          "0 - выход")

def show_message():
    input("Нажмите 'ENTER' для продолжения")

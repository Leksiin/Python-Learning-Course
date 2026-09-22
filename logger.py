import json
import os
import platform
import sys

import psutil

def main():
    data = search_data()
    save_data(data)

def search_data():
    comp_name = str(platform.node()) + str(os.getpid())
    logic_count = psutil.cpu_count()
    used_memory = psutil.virtual_memory().used
    total_memory = psutil.virtual_memory().total
    active_processes = psutil.process_pids()
    cpu_percent = psutil.cpu_percent(interval=1)
    disk_used = psutil.disk_usage("/").used
    cpu_speed = psutil.cpu_freq().current


    data = {
        "Имя Компа" : comp_name,
        "Логические процессы" : logic_count,
        "Использовано памяти" : used_memory,
        "Общая память" : total_memory,
        "Число активных процессов" : active_processes,
        "Загрузка процессора" : cpu_percent,
        "Занято памяти на HDR" : disk_used,
        "Скорость процессора" : cpu_speed
            }
    return data

def save_data(data:dict):
    name = "data.json"
    with open(name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

main()

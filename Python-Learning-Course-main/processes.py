"""Программа для работы с процессами
import subprocess
import os
import multiprocessing as mp
import time

def main():
    print("Starting")
    print(f"PID main: {os.getpid()}")
    print(f"PID parent main: {os.getppid()}")
    proc = mp.Process()
    proc.start()
    time.sleep(5)
    welcome()

def welcome():
    print("Hello")
    print(f"PID : {os.getpid()}")
    time.sleep(5)

def work():
    print("Working")
    print(f"PID : {os.getpid()}")
    time.sleep(5)
    finish()

def finish():
    print(f"PID : {os.getpid()}")
    time.sleep(5)
    print("Finished")

if __name__ == "__main__":
    main()"""

import asyncio # для асинхронности


async def task1(stop): # функция асинхронности
    await asyncio.sleep(stop) # время ожидания
    print("task 1") # вывод названия

async def task2(stop): # функция асинхронности
    await asyncio.sleep(stop) # время ожидания
    print("task 2") # вывод названия

async def task3(stop): # функция асинхронности
    await asyncio.sleep(stop) # время ожидания
    print("task 3") # вывод названия

async def main(): # функция для соеденения всех функций
    await asyncio.gather(task1(1), task2(1), task3(1))
asyncio.run(main()) # вывод


"""
Check this code to explain how asyncio works on long time tasks:


import asyncio # для асинхронности
import time


async def task1(stop): # функция асинхронности
    await asyncio.sleep(stop) # время ожидания
    time.sleep(2)
    print("task 1") # вывод названия

async def task2(stop): # функция асинхронности
    await asyncio.sleep(stop) # время ожидания
    time.sleep(3)
    print("task 2") # вывод названия

async def task3(stop): # функция асинхронности
    await asyncio.sleep(stop) # время ожидания
    time.sleep(4)
    print("task 3") # вывод названия

async def main(): # функция для соеденения всех функций
    await asyncio.gather(task1(1), task2(1), task3(1))
asyncio.run(main()) # вывод




Olso u can read about "time" lybrary if u aint know it
"""
try: # пробуем условие
    num = int(input('Введите число: '))
    print(num)
except ValueError: # если ошибка то выводим просьбу
    print('Ошибка: нужно ввести число! ')
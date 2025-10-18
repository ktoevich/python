data1 = input("Введите информацию")
data2 = input("Введите информацию №2")
data3 = input("Введите информацию №3")
file = open('data/notes.txt', 'a') # открывает файл для дабавления функций
file.write(f'{data1} {data2} {data3}\n') # добавляет информацию 1, 2, 3 в файл
file.close() # закрывает файл
file = open('data/notes.txt', 'r') # открывает файл для чтения
for line in file: #
    print(line)
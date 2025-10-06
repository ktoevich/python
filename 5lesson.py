for i in range(1, 21):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)

# Принты пиши более красивые и понятные на пример print(f"{i} Fizz") или print(f"{i} Buzz") и добавляй комментарии к коду (это хороший тон)
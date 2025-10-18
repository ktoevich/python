# чтение поля
board = [input().strip() for _ in range(3)]

# функция для проверки победителя
def winner(symbol):
    # строки и столбцы
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):  # строка
            return True
        if all(board[j][i] == symbol for j in range(3)):  # столбец
            return True
    # диагонали
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

# определяем победителя
x_win = winner('X')
o_win = winner('O')

if x_win:
    print("Win")
elif o_win:
    print("Lose")
else:
    print("Draw")

import print_task as pt

def menu():
    print(pt.hek())
    print(pt.menu_text())
    menu_task()

def menu_task():
    number = int(input('\033[32mВведите цифру выбранного варианта: \033[0m'))

    if 1 <= number <= 3:
        match number:
            case 1:
                print(pt.task1_text())
                matrix_start()
                menu_task()
            case 2:
                print(pt.task2_text())
                task2_start()
                menu_task()
            case 3:
                print(pt.task3_text())
                task3_start()
                menu_task()

    elif number == 00:
        print(pt.menu_text())
        menu_task()

    elif number == 0:
        print(pt.exin_text())
        exit()

    else:
        print(pt.error_text())
        menu_task()

# Задача 1
MATRIX = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
]

def matrix_start():
    print("\033[32mИсходная матрица:\033[0m\n")
    print_matrix(MATRIX)
    print("\n\033[32mТранспонированная матрица:\033[0m\n")
    print_matrix(transpose_matrix(MATRIX))

def print_matrix(matrix: list[list]):
    """Вывод квадратной матрицы на экран"""
    for row in matrix:
        print(row)

def transpose_matrix(matrix: list[list]) -> list[list]:
    """Транспонирование матрицы"""
    new_matrix = [[] for _ in range(0, len(matrix[0]))]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix[col].append(matrix[row][col])
    return new_matrix

# Задача 2
# добавлена для примешивания глобальной переменной
GLOBAL_VALUE = 23

def my_func(**kwargs) -> dict:
    """Функция подготовки словаря из переданных аргументов и их значений"""
    result = dict()
    for k, v in kwargs.items():
        try:
            _ = hash(v)
            result[v] = k
        except TypeError:
            result[str(v)] = k
    return result

def task2_start():
    print("Исх. параметры: first=\"one\", second=2, third=3, fourth=\"four\", fifth=[2, 3]")
    print(my_func(first="one", second=2, third=3, fourth="four", fifth=[2, 3]))

# Задача 3
summa = 0
LIST = ('50', '100', '150', '500', '1000', '5000', 'Другое', 'Выход')
percent = 1.5
count = 0
TAX = 10
operation = {}

def task_choice() -> str:
    print('Выберите следующие действия\n'
          '1: Пополнить\n'
          '2: Снять\n'
          '3: Выйти\n')
    choice = input('Введите номер действия: ').strip()
    while not choice.isdigit() or choice > '3':
        print('Выберите следующие действия\n'
              '1: Пополнить\n'
              '2: Снять\n'
              '3: Выйти\n')
        choice = input('Введите номер действия: ').strip()
    return choice

def account_replenishment() -> None | object:  # Пополнение счета
    global summa, LIST, percent, count, TAX, operation
    print(f'Ваш баланс на данный момент составляет {summa}')
    if summa > 5_000_000:
        percent = TAX
    if count % 3 == 0:
        percent += 3
    print('Доступные варианты')
    [print(f'{v}', end='   ') if i != 2 and i != len(LIST) - 1 else print(
        f'{v}') for i, v in enumerate(LIST)]
    replenish = input('Введите число для пополнение: ').strip()
    while replenish not in LIST:
        print('Доступные варианты')
        [print(f'{v}', end='   ') if i != 2 and i != len(LIST) - 1 else print(
            f'{v}') for i, v in enumerate(LIST)]
        replenish = input('Введите число для пополнение: ').strip()
    if replenish.isdigit():
        if replenish in LIST:
            summa += int(replenish)
            print(f'Ваш баланс на данный момент составляет {summa}')
            count += 1
            operation.setdefault('Пополнение', []).append(replenish)
        else:
            print('Данное число не найдено')
    elif replenish == 'Другое':
        try:
            replenish = int(
                input("Введите другое число для пополнение: ").strip())
            summa += int(replenish)
            operation.setdefault('Пополнение', []).append(replenish)
            count += 1
            print(f'Ваш баланс на данный момент составляет {summa}')
        except ValueError:
            print('Был введён не корректный символ\nЗавершение программы...')
            menu_task()
    elif replenish == 'Выход':
        return task_choice()

def account_withdrawal() -> None | object:  # Снятие денег
    global summa, LIST, percent, count, TAX, operation
    print(f'Ваш баланс на данный момент составляет {summa}')
    if summa > 5_000_000:
        percent = TAX
    if count % 3 == 0:
        percent += 3
    print('Доступные варианты')
    [print(f'{v}', end='   ') if i != 2 and i != len(LIST) - 1 else print(
        f'{v}') for i, v in enumerate(LIST)]
    replenish = input('Введите число для снятие наличных: ').strip()
    while replenish not in LIST:
        print('Доступные варианты')
        [print(f'{v}', end='   ') if i != 2 and i != len(LIST) - 1 else print(
            f'{v}') for i, v in enumerate(LIST)]
        replenish = input('Введите число снятие наличных: ').strip()
    if replenish.isdigit():
        if replenish in LIST:
            if summa - int(replenish) < 0:
                print("Не достаточно средств")
            else:
                replenish = int(replenish)
                summa -= replenish + (30 if (s := ((
                                                    replenish / 100) * percent))
                                                < 30 else 600 if s > 600 else s)
                summa = f'{summa:.2f}'
                summa = float(summa)
                operation.setdefault('Снятие', []).append(replenish)
                print(f'Ваш баланс на данный момент составляет {summa}')
                count += 1
        else:
            print('Данное число не найдено')
    elif replenish == 'Другое':
        try:
            replenish = int(
                input("Введите другое число снятие наличных: ").strip())
            if summa - int(replenish) < 0:
                print("Не достаточно средств")
            else:
                replenish = int(replenish)
                summa -= replenish + (30 if (s := ((
                                            replenish / 100) * percent))
                                            < 30 else 600 if s > 600 else s)
                summa = f'{summa:.2f}'
                summa = float(summa)
                operation.setdefault('Снятие', []).append(replenish)
                count += 1
                print(f'Ваш баланс на данный момент составляет {summa}')
        except ValueError:
            print('Был введён не корректный символ\nЗавершение программы...')
            menu_task()
    elif replenish == 'Выход':
        return task_choice()

def action(num: str) -> object | str:
    if num == '1':
        return account_replenishment()
    elif num == '2':
        return account_withdrawal()
    else:
        return 'Завершение программы'

def task3_start() -> object | str:
    flag = task_choice()
    while flag < '3':
        check = action(flag)
        if check is not None:
            flag = check
        else:
            flag = task_choice()

    else:
        print("Завершение программы")
        menu_task()
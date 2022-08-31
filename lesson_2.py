# Exercise 1
# def isfloat(y):
#     try:
#         float(y)
#     except ValueError:
#         return False
#     return True
#
#
# n = 0
# while n < 3:
#     x = input('Введите вещественное число = ')
#     if not isfloat(x):
#         print('Введено не вещественное число')
#     else:
#         print(f'Сумма цифр числа {sum(map(int, str(abs(float(x))).replace(".", "")))}')
#     n += 1

# Exercise 2
def isint(y):
    try:
        int(y)
    except ValueError:
        return False
    return True
#
#
# n = 0
# count = 1
# arr = []
# while n < 3:
#     x = input('Введите целое число = ')
#     if not isint(x):
#         print('Введено не целое число')
#     else:
#         for i in range(1, int(x)+1):
#             count *= i
#             arr.append(count)
#         print(f'Вектор значений {arr}')
#     n += 1

# Exercise 3
n = 0
count = 0
arr = []
while n < 3:
    x = input('Введите целое число = ')
    if not isint(x):
        print('Введено не целое число')
    else:
        for i in range(1, int(x)+1):
            ch = (1 + 1 / i) ** i
            arr.append(ch)
            count += ch
        print(f'Вектор значений {arr}')
        print(f'Сумма значений вектора {count}')
    n += 1

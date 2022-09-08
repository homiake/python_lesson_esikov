def isint(y):
    try:
        int(y)
    except ValueError:
        return False
    return True


# Exercise 1
n = 0
while n < 3:
    count = 0
    x = input('Введите несколько чисел через пробел = ')
    a = x.split(' ')
    if len(a) > 1:
        for i in range(1, len(a), 2):
            count += int(a[i])
        print(f'Сумма элементов списка, стоящих на нечётной позиции = {count}')
    else:
        print('Введённые данные некорректны')
    n += 1

# Exercise 2
n = 0
while n < 3:
    count = []
    x = input('Введите несколько чисел через пробел = ')
    a = x.split()
    s = (len(a)//2) if (len(a) % 2 == 0) else (len(a)//2 + 1)
    if len(a) > 1:
        for i in range(s):
            print(f'i = {i} -> {int(a[i])} * {int(a[len(a)-1-i])}')
            count.append(int(a[i])*int(a[len(a)-1-i]))
        print(f'Произведение пар чисел списка = {count}')
    else:
        print('Введённые данные некорректны')
    n += 1

# Exercise 3
n = 0
while n < 3:
    count = ''
    x = input('Введите число для перевода в двоичную систему = ')
    if isint(x):
        x = int(x)
        while x > 0:
            count += str(x % 2)
            x //= 2
        print(f'Произведение пар чисел списка = {count[::-1]}')
    else:
        print('Введённые данные некорректны')
    n += 1

# Exercise 4
n = 0
while n < 3:
    count = []
    x = input('Введите размер массива членов Фибоначчи = ')
    if isint(x):
        fib1 = 0
        fib2 = 1
        arr = [fib1, fib2]
        res_arr = []
        for i in range(int(x) - 1):
            fib_sum = fib1 + fib2
            fib1 = fib2
            fib2 = fib_sum
            arr.append(fib_sum)
        for j in range(len(arr) - 1, 0, -1):
            if j % 2 == 0:
                res_arr.append(-arr[j])
            else:
                res_arr.append(arr[j])
        res_arr += arr
        print(f'Список чисел Фибоначчи = {res_arr}')
    else:
        print('Введённые данные некорректны')
    n += 1

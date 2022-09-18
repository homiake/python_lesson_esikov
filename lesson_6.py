# Exercise 1
import random

def checkx(pole):
    if pole[0][0] == 'X' and pole[0][1] == 'X' and pole[0][2] == 'X':
        print('x wins')
        return True
    if pole[1][0] == 'X' and pole[1][1] == 'X' and pole[1][2] == 'X':
        print('x wins')
        return True
    if pole[2][0] == 'X' and pole[2][1] == 'X' and pole[2][2] == 'X':
        print('x wins')
        return True
    if pole[0][0] == 'X' and pole[1][0] == 'X' and pole[2][0] == 'X':
        print('x wins')
        return True
    if pole[0][1] == 'X' and pole[1][1] == 'X' and pole[2][1] == 'X':
        print('x wins')
        return True
    if pole[0][2] == 'X' and pole[1][2] == 'X' and pole[2][2] == 'X':
        print('x wins')
        return True
    if pole[0][0] == 'X' and pole[1][1] == 'X' and pole[2][2] == 'X':
        print('x wins')
        return True
    if pole[2][0] == 'X' and pole[1][1] == 'X' and pole[0][2] == 'X':
        print('x wins')
        return True
    if pole[0][0] == 'Y' and pole[0][1] == 'Y' and pole[0][2] == 'Y':
        print('y wins')
        return True
    if pole[1][0] == 'Y' and pole[1][1] == 'Y' and pole[1][2] == 'Y':
        print('y wins')
        return True
    if pole[2][0] == 'Y' and pole[2][1] == 'Y' and pole[2][2] == 'Y':
        print('y wins')
        return True
    if pole[0][0] == 'Y' and pole[1][0] == 'Y' and pole[2][0] == 'Y':
        print('y wins')
        return True
    if pole[0][1] == 'Y' and pole[1][1] == 'Y' and pole[2][1] == 'Y':
        print('y wins')
        return True
    if pole[0][2] == 'Y' and pole[1][2] == 'Y' and pole[2][2] == 'Y':
        print('y wins')
        return True
    if pole[0][0] == 'Y' and pole[1][1] == 'Y' and pole[2][2] == 'Y':
        print('y wins')
        return True
    if pole[2][0] == 'Y' and pole[1][1] == 'Y' and pole[0][2] == 'Y':
        print('y wins')
        return True


pole = [['_' for x in range(3)] for y in range(3)]

for i in pole:
    print(*i)

while not checkx(pole):
    a, b = int(input()), int(input())
    pole[a][b] = 'X'

    for i in pole:
        print(*i)

    while True:
        c, d = random.randint(0, 2), random.randint(0, 2)
        if pole[c][d] != 'X' and pole != 'O':
            pole[c][d] = 'O'
            break
    for i in pole:
        print(*i)

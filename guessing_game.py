from random import *


print('Добро пожаловать в числовую угадайку')
right = int(input('Введите число ограничитель: '))
num = randint(1, right)
count = 0
def is_valid(n):
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 100:
            return True
        else:
            return False
    else:
        return False

while True:
    n = input(f'Введите число от 1 до {right}: ')
    if is_valid(n) != True:
        print(f'А может быть все-таки введем целое число от 1 до {right}?')
        continue
    else:
        n = int(n)

    if n == num:
        print('Вы угадали, поздравляем!')
        count += 1
        break
    elif n < num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count += 1
    elif n > num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        count += 1

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

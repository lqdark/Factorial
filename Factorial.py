# -*- coding: cp1251 -*-
import math

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print('=====================================')
print('Программа вычисления факториала числа')
print('=====================================')

x=0
while x != 1:
    number = input('Введите положительное целое число: ')
    if isint(number):
        if int(number) > 0:
            x = 1;
        else:
            print("Вы ввели отрицатльное число, повторите ввод.")
    else:
        print('Ошибка ввода. Введите  число.')
        

result = math.factorial(int(number))
print("Факториал числа", number, "равен", result)
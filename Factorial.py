# -*- coding: cp1251 -*-
import math

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print('=====================================')
print('��������� ���������� ���������� �����')
print('=====================================')

x=0
while x != 1:
    number = input('������� ������������� ����� �����: ')
    if isint(number):
        if int(number) > 0:
            x = 1;
        else:
            print("�� ����� ������������ �����, ��������� ����.")
    else:
        print('������ �����. �������  �����.')
        

result = math.factorial(int(number))
print("��������� �����", number, "�����", result)
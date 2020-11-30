import time

print(time.ctime())
print('Выполнил студент ИСТ-01 Крицкова')

# input('задача 1')
# try:
#   import math
#
#   a=float(input('введите первый катет '))
#  b=float(input('введите второй катет '))
# c=math.sqrt(a**2+b**2)
# print('гипотенуза равна :', c)
# except ValueError as v:
#   print("введите число")
#  print(v)


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


try:
    a = input('введите слово : ')
    if not is_number(a):
        print(len(a))
    else:
        raise Exception('Вы ввели число')
except Exception as e:
    print(e)


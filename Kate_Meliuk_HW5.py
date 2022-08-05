#1 Напишите функцию, которая принимает два числа в кач-ве аргументов и считает наименьшее общее кратное для этих чисел.
'''def x(a,b):
    if b == 0:
        return a
    return x(b, a%b)
a, b = map(int, input('Введите два числа ').split())
print(a*b//x(a,b))'''

#2 Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
'''def sum_range(start, end):
    if start > end:
        start, end = end, start
    s = 0
    for i in range(start, end + 1):
        s += i
    return s


a, b = map(int, input("Введите два целых числа: ").split())
print(sum_range(a, b))'''

#3 Написать программу, которая посчитает кол-во одинаковых элементов в списке.
# Список будет заполняться рандомными целыми числами.
# Рекомендую использовать несколько функций
# (для заполнения списка целыми числами, для подсчета количества, для вывода)
'''from random import random
def create_rand_list() -> list:
    rand_list = []
    for i in range(len_list):
        rand_list.append(int(random()*100))
    return rand_list

print(create_rand_list(10))'''
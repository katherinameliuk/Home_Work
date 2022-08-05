# 1. Вы вводите с клавиатуры последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.
'''numbers = input('Input numbers: ')
lst_nums = numbers.split(',')
tpl_nums = tuple(lst_nums)
print(lst_nums, tpl_nums)'''

# 2. Напишите программу, которая проверяет является ли число четным.
'''number = int(input('Input numbers: '))
if number % 2 == 0:
    print(f'{number} is eve.')
else:
    print(f'{number} is odd.')'''

# 3. Есть две переменных x, y. Поменяйте значения переменных местами.
'''x = 1
y = 2
x, y =y, x
print(x, y)'''

# 4. Написать программу, которая удаляет первый и последний символы строки.
# Если строка содержит меньше  двух символов - вывести сообщение об ошибке.
'''foo = input('input string: ')

if len(foo) > 2:
    foo = foo[ 1:-1]
    print(foo)
else:
    print('Error')'''
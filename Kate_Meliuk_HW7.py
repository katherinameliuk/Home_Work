#  Написать функцию, которая на вход принимает целое число n,
# а возвращает n первых чисел из последовательности Фибоначчи.
def Fib(n: int):
    f1 = f2 = 1
    i = 0
    while (i < n):  # с помощью цикла вычисляем числа Фибоначчи
        i += 1
        s = f1 + f2
        f1 = f2
        f2 = s
        print(s)  # Печатаем числа


Fib(10)
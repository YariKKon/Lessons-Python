# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

n = str(input('Enter any number to get the sum of the digits: '))
sum = 0
for elem in n:
    if elem.isdigit():
        sum += int(elem)
print("The sum of the digits of a given number: ", sum) 

# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Enter any number N: '))
result = 1
for i in range(1, n+1):
    result *= i
    print(result, end=' ')
    
# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}



n = int(input('Enter a number: ')) 

def get_squerence(n):
    return [round((1 + 1 / n)**n, 5) for n in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 5))
    
# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

import datetime 

min_n = 1
max_n = 100

def get_rand():
    return datetime.datetime.now().microsecond%10

n = get_rand()


print(n)
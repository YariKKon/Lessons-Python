# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# a = int(input('Введите 1 число: '))
# b = int(input('Введите 2 число: '))

# if a ** 2 == b:
#      print('да')
# elif b ** 2 == a:
#      print('да')
# else:
#      print('нет')    


# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# list_numbers = [1, 4, 8, 7, 5]
# max_num = list_numbers[0]
# for item in list_numbers:
#     if max_num < item:
#         max_num = item
# print(max_num)     


# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# *Примеры:*

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5



# number = int(input("Enter number: "))

# if number < 0:
#     number = -number

# list_numbers = []

# for num in range(-number, number +1):
#     list_numbers.append(num)

# print(list_numbers)    



#  2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3


number = float(input("enter number: "))
if number - int(number) == 0: print('No')

else:
    answer = number * 10 % 10
    print(int(answer))
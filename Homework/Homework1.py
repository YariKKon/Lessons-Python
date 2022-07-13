# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day = int(input('Input the number of the day of the week: '))

# if day < 1 or day > 7:
#     print(day, '-> Incorect number of day!!!')
# elif day > 5 & day < 8:
#     print(day,'-> Weekend')
# else:
#     print(day,'-> Weekday')    

# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = (input('Input x-coordinate -> '))
# y = (input('Input y-coordinate -> '))

# def define_quarter(x, y):

#     try:
#         x = int(x)
#     except:
#         return 'Incorrect input: enter an integer'
#     try:
#         y = int(y)
#     except:
#         return 'Incorrect input: enter an integer'
#     if(x > 0 and y > 0):
#         return f'x = {x}; y = {y} -> 1'
#     elif(x < 0 and y > 0):
#         return f'x = {x}; y = {y} -> 2'
#     elif(x < 0 and y < 0):
#         return f'x = {x}; y = {y} -> 3'
#     elif(x > 0 and y < 0):
#         return f'x = {x}; y = {y} -> 4'
#     else:
#         return 'By the condition of the task, X is not equal to 0 and Y is not equal to 0'

# print(define_quarter(x, y))


#4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# quarter_number = int (input("Input quarter number: "))

# def coordinates(qvad):

    
#     if(qvad == 1):
#         return "x > 0, y > 0"
#     elif(qvad == 2):
#         return "x < 0, y > 0"
#     elif(qvad == 3):
#         return "x < 0, y < 0"
#     elif(qvad == 4):
#         return "x > 0, y < 0"
#     else:
#         return "Wrong number!"                

# print(coordinates(quarter_number))

# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# x1 = int(input('Enter coordinates X for point A = '))
# y1 = int(input('Enter coordinates Y for point A = '))
# x2 = int(input('Enter coordinates X for point B = '))
# y2 = int(input('Enter coordinates Y for point B = '))
# result = ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
# print(round(result, 2))
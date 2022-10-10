# a = int(input("Введите номер дня недели: "))
# if a > 1 and a <= 5:
#     print("Это рабочий день")
# elif a > 5 and a <=7:
#     print("Это выходной")
# else:
#     print("В неделе семь дней!!!")


# print("Введите координаты точки")
# x = int(input("X = "))
# y = int(input("Y = "))
# if x>0 and y >0:
#     print("Точка в I четверти")
# elif x>0 and y <0:
#     print("Точка в IV четверти")
# elif x<0 and y <0:
#     print("Точка в III четверти")
# elif x<0 and y >0:
#     print("Точка в II четверти")


# x = int(input('Введите число x '))
# y = int(input('Введите число y '))
# z = int(input('Введите число z '))
# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print(not (x or y or z) == (not x and not y and not z))
#                 print(x, y, z)

#
# h = int (input('Введите номер четверти: '))
# if h == 1:
#     print ('X > 0, Y > 0')
# elif h == 2:
#     print('X < 0, Y > 0')
# elif h == 3:
#     print('X < 0, Y < 0')
# elif h == 4:
#     print('X > 0, Y < 0')
# else:
#     print('Введите число от 1 до 4!!!!')

import math
print('Введите координаты двух точек')
x1 = int(input('X = '))
y1 = int(input('Y = '))
x2 = int(input('X = '))
y2 = int(input('Y = '))
c = round(math.sqrt(((x1-x2)**2) + ((y1-y2)**2)), 2)
print(f'Расстояние между точками {c}')
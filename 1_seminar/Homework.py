# №1 Задача
#number = int(input('Введите порядковый номер дня недели и узнаете является ли день выходным: '))
#
#if 8 > number > 5:
#    print("Да, день выходной")
#elif 6 > number > 0:
#    print('Нет, день будний')
#else:
#    print("Вы ошиблись с номером дня недели, извините.")
#
# №2  Задача
#
#
# №3  Задача
#
print('Введите значения координат x и y точки и узнаете в какой четверти оси координат находится данная точка!')
x = float(input('Введите значение x - '))
y = float(input('Введите значение y - '))

if x > 0 and y > 0:
    print('Данная точка находится в 1 четверти оси координат')
elif x < 0 and y > 0:
    print('Данная точка находится во 2 четверти оси координат')
elif x < 0 and y < 0:
    print('Данная точка находится в 3 четверти оси координат')
elif x > 0 and y < 0:
    print('Данная точка находится в 4 четверти оси координат')
else:
    print('Данная точка не принадлежит ни к одной из четвертей')

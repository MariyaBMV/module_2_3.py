 #DZ
"""Задача "Нули ничто, отрицание недопустимо!":
Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или не закончитс
я список (выход за границу).

Пункты задачи:
Запишите исходный список в переменную my_list.
Напишите цикл while с соответствующими задаче условиями.
Используйте операторы прерывания/продолжения цикла в соответствии с условиями задачи."""

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5] #создали список my_list
a = len(my_list)  #с помощью функции len выявила количество элементов в списке и поместила ее в переменную a.
b = 0  #объвила переменную b присвоила ей значение 0, чтобы перебрать список по индексу


while a != b:  # создали цикл while чтобы перебрать в цикле список my_list по индексу перебераем список while.
      c = my_list[b] # получили содержание ячейки списка по индексу
      b = b + 1 # увеличили каждый цикл на 1.
      if  c > 0:   # создала условие при котором будут перебираться элементы списка и выводится на консоль элементы больше 0.
            print(c)  # вывели на консоль элементы, которые соответствуют заявленному условию.
      elif c == 0:
            continue
      else: # если условие не выполняется, программа завершается командой break
            break #завершение программы.




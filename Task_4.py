# Задача 4. 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2 
# Позиции: 0,1 -> 2

n = int(input('Введите число: '))
new_list = list(range(-n, n+1))
print(new_list)

numbers = input('Введите позиции 2х чисел через пробел: ')
num = numbers.split()
a = int(num[0])-1
b = int(num[1])-1


if 0 <= a <= n*2 and 0 <= b <= n*2:
    mult = new_list[a] * new_list[b]
    print(
        f'Произведение чисел {new_list[a]} и {new_list[b]}, находящихся на {num[0]} и {num[1]} позициях, равно {mult}')
else:
    print(
        f'Для чисел в диапазоне от {-n} до {n} необходимо ввести номера позиций от 1 до {n*2+1}')
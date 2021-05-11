import random as rnd


##Вариант 14

## задание 7
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
i=1
while (i <= 13):
    print (fibonacci(i))
    i+=1

## задание 9
try:
    a = int(input("Введите первое целое число: "))
    b = int(input("Введите второе целое число: "))
    h = int(input("Напишите результат произведения: "))
    res = a * b
    if res == h:
        print("Верно")
    else:
        print("Ошибка, правильный ответ: ", res)
except:
    print("Ошибка при вводе данных!")

## задание 10
def mass(n):
    arr = []
    for i in range(n):
        arr.append(rnd.random())
    a = (max(arr), min(arr))
    return arr, a


n = int(input("Введите размерность массива: "))
mat, a = mass(n)
print("Массив: ", mat)
print("Макс. и Мин. значения в кортеже: ", a)

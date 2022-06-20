""" def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # прямая передача значений

x = 5
y = 7
print_max(x, y)  # передача переменных в качестве аргументов """

""" def plus(a, b):
  c = a + b
  return c

res = plus(3, 4)
print(res)  # Выведет 7 """

""" #Ключевые аргументы 
def func(a, b=5, c=10): #Значениями по умолчанию могут быть снабжены только параметры, находящиеся в конце списка параметров.
    print('a равно', a,', b равно', b,', а c равно', c)

func(3, 7)          # a равно 3, b равно 7, а c равно 10
func(25, c=24)      # a равно 25, b равно 5, а c равно 24
func(c=50, a=100)   # a равно 100, b равно 5, а c равно 50 """

""" def say(message, times=1):
    print(message * times)

say('Привет')   # Привет
say('Мир', 5)   # МирМирМирМирМир """

# Переменное число параметров


""" 
def total(a=5, *numbers, **phone_book):
    print('a', a)
    # проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)
    print(numbers)

    #проход по всем элементам словаря
    for first_part, second_part in phone_book.items():
        print(first_part,second_part)
    print(phone_book)

print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
 """

""" # Кортежи
not_empty = (2, 4, 6)
def my_tuple (a=0):
    print (not_empty[a])

for i in range(len(not_empty)):
    my_tuple(i) """

""" #Словари
new_key_out = ""
new_value_out = ""
not_empty = {"key": "value"}
def add_dict (new_key, new_value):
    not_empty[new_key] = new_value
    print(not_empty)    # {"key": "value", "new_key": "new value"}

#input(f"New key {new_key_out}")
#input (f"New value {new_value_out}")  
add_dict(input("Enter Key"), input("Enter Value")) 
 """
# Рекурсия
""" def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

for i in range (0,10):

    print(factorial(i+1))   # 120 """

# Импорт пакетов и модулей
""" import math
sin_pi = math.sin(math.pi)
print(math.pi)
print(sin_pi)


from math import pi, sin
sin_pi = sin(pi) """

# Импорт собственных модулей
from hello import say_hello

print("You imported hello.py")
say_hello('user')

#Точка входа

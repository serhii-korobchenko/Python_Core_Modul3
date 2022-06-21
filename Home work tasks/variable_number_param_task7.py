""" Следующая задача будет сугубо теоретической, и мы потренируемся работать с произвольным 
количеством аргументов.

Создайте две функции:

первая first будет иметь первым параметром переменную size, а также она может принимать 
любое количество позиционных аргументов. Функция должна вернуть сумму size c общим 
количеством переданных в нее позиционных аргументов.
вторая функция second так же будет иметь первым параметром size и будет принимать 
произвольное количество ключевых аргументов, и также должна вернуть сумму сложения 
size c количеством переданных в функцию ключевых аргументов.
Тестовые вызовы функций, для правильности работы, будут следующими:

first(5, "first", "second", "third")
first(1, "Alex", "Boris")
second(3, comment_one="first", comment_two="second", comment_third="third")
second(10, comment_one="Alex", comment_two="Boris") """

def first(size, *my_tuple):
    return size + len(my_tuple)
    
def second(size,**my_dict):
    return size + len(my_dict)

print (first(5, "first", "second", "third"))
print (second(3, comment_one="first", comment_two="second", comment_third="third"))
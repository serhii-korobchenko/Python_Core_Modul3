""" Для функции из предыдущей задачи создайте строки документации. 
Можно использовать следующий шаблон """

"""Функция возвращает общую сумму доставки.

    Первый параметр &mdash; количество товаров в заказе.
    Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0."""



def cost_delivery(quantity, *_, discount=0):
    """ Function calculate delivery cost.

    First parametr (quantity) - reveal quantity items in order. 
    Parametr (discount) represent discount rate (0-1). """
    
    
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result


print(cost_delivery.__doc__)

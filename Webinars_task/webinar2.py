""" # Функція приймає рядок, а повертає словник, де ключ це символ рядка, а значення код ASCII
# {'key': 'value'}

def convert(value_str: str) -> dict:
    data = {}
    for ch in value_str:
        if not ch in data:
            data[ch] = ord(ch)   # {'ch': 'ord(ch)'}
    return data


print(convert("Hello world")) """

""" # Написати функцію для визначення, чи є число простим?

def is_num(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def main():
    value = int(input("Please set int number: "))
    if is_num(value):
        print(f"{value} is simple number")
    else:
        print(f"{value} is not simple number")


if __name__ == "__main__":
    main()
 """

""" def convert_to_seconds(seconds=0, minutes=0, hours=0, days=0, week=0):
    number_seconds_in_minutes = 60  # const
    number_seconds_in_hours = 60 * number_seconds_in_minutes
    number_seconds_in_days = 24 * number_seconds_in_hours
    number_seconds_in_weeks = 7 * number_seconds_in_days
    res = seconds + minutes * number_seconds_in_minutes + \
           hours * number_seconds_in_hours + \
           days * number_seconds_in_days + \
           week * number_seconds_in_weeks \

    return res """


""" 
print(convert_to_seconds(minutes=5, days=1, week=1)) """


def factorial(n):

    if n== 0:
        return 1

    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):

    return factorial(n) 


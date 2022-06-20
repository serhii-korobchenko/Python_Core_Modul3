""" во время импорта функции say_hello из hello.py код в блоке if ... не будет выполнен, 
а если же в консоли выполнить python hello.py, то будет.
Для удобства принято весь код, который надо выполнить, когда модуль вызывается из консоли (не импортируется), 
помещать в функцию main: """

import sys

def say_hello(name):
    print(f'Hello {name}')



def main():
    print("You imported hello.py")
    say_hello('user')

for arg in sys.argv:
    print(arg)
if __name__ == '__main__':
    main()
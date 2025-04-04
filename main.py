from avocado import Avocado
from log import logging

@logging
def fr():
    print('Hello World!')

def sec():
    arc = Avocado('avocado.csv')
    arc.paint()


def main():
    usr_ch = input('Write 1 if you want to see the first task, and 2 if the second')
    if usr_ch == '1':
        fr()
    elif usr_ch == '2':
        sec()
    else:
        print('Не надо так делать пожалуйста, пиши уже нормально')


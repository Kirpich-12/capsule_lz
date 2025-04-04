from avocado import Avocado
from log import logging

@logging
def avoc():
    arc = Avocado('avocado.csv')
    arc.paint()

def main():
    avoc()

if __name__ == '__main__':
    main()
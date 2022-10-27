import utils
from utils import print_hello
from utils import print_hello as ph

import my_stuff.utils2
from my_stuff.utils2 import other_print
import my_package

from math import cosh, sqrt


def print_hello(name):
    print(f'Hahaha {name}')


utils.print_hello('Anna')  # Uses import utils
print_hello('Bob')         # Uses from utils import print_hello
ph('Carl')                 # Uses from utils import print_hello as ph

my_stuff.utils2.other_print('Hi', 'Dina')
other_print('Yo', 'Miles')

my_package.say_hello()
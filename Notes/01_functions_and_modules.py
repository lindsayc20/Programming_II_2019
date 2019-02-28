import random
from math import pi as Samuel   # import one object
from math import *
from my_import import *


if __name__ == "__main__":
    '''
    this code runs when I execute THIS file
    '''
    say_hi()
    my_cube = cube(3)
    print(my_cube)
    print(cube(random.randrange(1, 101, 3)))  # odd int from 1 to 100
    print(random.random())  # float from 0 to 1
    print(Samuel)
    print(cos(2))

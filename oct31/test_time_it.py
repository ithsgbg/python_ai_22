from time_it import time_it
from time import sleep


@time_it
def time_me(s):
    sleep(s)


@time_it
def second_func(s):
    sleep(s)


def main():
    time_me(3)
    second_func(2)


if __name__ == '__main__':
    main()
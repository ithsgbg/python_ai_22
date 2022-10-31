def my_range(n):
    value = 0
    
    while value < n:
        yield value
        value += 1


def my_gen(n):
    print('starting generator')
    yield n
    n += 1
    yield n
    n += 1
    yield n


def main():
    # g = my_gen(10)
    # print(next(g))
    # print(next(g))
    # print(next(g))
    # print(next(g))
    for i in my_range(10):
        print(i)


if __name__ == '__main__':
    main()